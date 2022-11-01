# fastapi
from fastapi import Depends

from fastapi.responses import JSONResponse

#discord
from fastapi_discord import User, DiscordOAuthClient, RateLimited, Unauthorized
from fastapi_discord.exceptions import ClientSessionNotInitialized, InvalidToken


#local
from . import router
from base.settings import app
from all_env import CLIENT_ID, CLIENT_SECRET, REDIRECT_URL
from .models import DiscordUser


discord = DiscordOAuthClient(
    CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, 
    ("identify", "guilds", "email")
)  # scopes

# start
@router.on_event("startup")
async def on_startup():
    await discord.init()


@router.get("/discord_oauth")
async def discord_oauth(code: str):
    token, refresh_token = await discord.get_access_token(code)
    return {"access_token": token, "refresh_token": refresh_token}

@router.get("/discord_user", dependencies=[Depends(discord.requires_authorization)], response_model=DiscordUser)
async def get_user(user: User = Depends(discord.user)):

    discord_user = DiscordUser(
        id=user.id,
        email=user.email,
        name=user.username,
        avatar_url=user.avatar_url
    )
    if discord_user.update():
        return JSONResponse(discord_user.__dict__, status_code=200)

    return JSONResponse(discord_user.__dict__, status_code=400)


#exception
@app.exception_handler(Unauthorized)
async def unauthorized_error_handler(_, __):
    return JSONResponse({"error": "Unauthorized"}, status_code=401)


@app.exception_handler(RateLimited)
async def rate_limit_error_handler(_, e: RateLimited):
    return JSONResponse(
        {"error": "RateLimited", "retry": e.retry_after, "message": e.message},
        status_code=429,
    )


@app.exception_handler(ClientSessionNotInitialized)
async def client_session_error_handler(_, e: ClientSessionNotInitialized):
    print(e)
    return JSONResponse({"error": "Internal Error"}, status_code=500)


@app.exception_handler(InvalidToken)
async def invalid_token(_, e: InvalidToken):
    print(e)
    return JSONResponse({"error": "Invalid Token"}, status_code=500)
