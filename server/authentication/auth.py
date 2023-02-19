# fastapi
from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import EmailStr

# default
from typing import Optional

# local
from . import router
from .schemas import User
from .jwt_auth import auth_handler
from .google_oauth import GoogleOauth2
from .facebook_oauth import FaceBookOauth2

from models import Users
from other_modules.time_modules import vn_now
from other_modules.json_modules import mongodb_to_json
from all_env import DISCORD_OAUTH_URL


@router.post("/register", status_code=201)
async def register(user: User):

    user_exist = await Users.find_one(Users.email == user.email)
    if user_exist:
        raise HTTPException(status_code=400, detail="email is taken")

    hashed_password = auth_handler.get_password_hash(user.password)
    user = Users(
        email=user.email,
        password=hashed_password,
        user_type="normal",
        name=user.name,
    )
    await user.insert()
    return JSONResponse(status_code=201, content=mongodb_to_json(user.get_info()))


@router.post("/login")
async def login(
    email: Optional[EmailStr] = None,
    password: Optional[str] = None,
):
    # authorize and get JWT token
    user = await Users.find_one(Users.email == email)
    if not user:
        raise HTTPException(status_code=404, detail="User not exist")
    elif not auth_handler.verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email and/or password")

    user.last_logged_in_at = vn_now()
    await user.save()

    token = auth_handler.encode_token(mongodb_to_json(user.get_info()))
    return {"token": token}


@router.get("/self", dependencies=[Depends(auth_handler.auth_wrapper)])
def protected(user: Users = Depends(auth_handler.auth_wrapper)):
    return user


@router.get("/oauth-link")
async def get_oauth_link(
    discord_link: Optional[bool] = False,
    google_link: Optional[bool] = False,
    facebook_link: Optional[bool] = False,
):
    response = {}
    if discord_link:
        response["discord_link"] = DISCORD_OAUTH_URL
    if google_link:
        response["google_link"] = GoogleOauth2().get_oauth_url()
    if facebook_link:
        response["facebook_link"] = FaceBookOauth2().get_oauth_url()

    return JSONResponse(response, status_code=200)
