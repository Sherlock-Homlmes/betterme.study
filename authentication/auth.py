# fastapi
from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import EmailStr

# default
from typing import Optional

# local
from . import router
from .schemas import Users, UsersInfo
from .jwt_auth import AuthHandler
from other_modules.time_modules import time_to_str
from all_env import DISCORD_OAUTH_URL
from .google_oauth import GoogleOauth2
from .facebook_oauth import FaceBookOauth2

auth_handler = AuthHandler()
users_list = []

@router.post('/register', status_code=201)
def register(users: Users):
    if any(x['email'] == users.email for x in users_list):
        raise HTTPException(status_code=400, detail='email is taken')
    hashed_password = auth_handler.get_password_hash(users.password)
    users_list.append({
        'email': users.email,
        'password': hashed_password    
    })
    return users_list


@router.post('/login')
def login(
        email: Optional[EmailStr] = None,
        password: Optional[str] = None,
        discord_token: Optional[str] = None,
        google_token: Optional[str] = None,
        facebook_token: Optional[str] = None,
    ):

    if email and password:
        user = None
        for x in users_list:
            if x['email'] == email:
                user = x
                break

        if (not auth_handler.verify_password(password, user['password'])):
            raise HTTPException(status_code=401, detail='Invalid email and/or password')

        current_user = UsersInfo(id=1, email=email)
        current_user.joined_at, current_user.last_logged_in_at = time_to_str(current_user.joined_at), time_to_str(current_user.last_logged_in_at)
        token = auth_handler.encode_token(current_user.__dict__)
        return { 'token': token }

    elif discord_token:
        pass

    elif google_token:
        pass
    
    elif facebook_token:
        pass

    raise HTTPException(status_code=401, detail='Invalid email and/or password')

@router.get('/self', dependencies=[Depends(auth_handler.auth_wrapper)])
def protected(user: Users = Depends(auth_handler.auth_wrapper)):
    return user

@router.get('/oauth-link')
async def get_oauth_link(
    discord_link: bool,
    google_link: bool,
    facebook_link: bool
):
    response = {}
    if discord_link:
        response['discord_link'] = DISCORD_OAUTH_URL
    if google_link:
        response['google_link'] = GoogleOauth2().get_oauth_url()
    if facebook_link:
        response['facebook_link']= FaceBookOauth2().get_oauth_url()
    
    return JSONResponse(response, status_code=200)
