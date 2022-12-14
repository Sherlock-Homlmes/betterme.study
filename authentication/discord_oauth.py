# fastapi
from fastapi import Depends

#discord
from fastapi_discord import User, DiscordOAuthClient

#local
from . import router
from base.settings import app
from all_env import DISCORD_CLIENT_ID, DISCORD_CLIENT_SECRET, DISCORD_REDIRECT_URL


discord = DiscordOAuthClient(
    DISCORD_CLIENT_ID, DISCORD_CLIENT_SECRET, DISCORD_REDIRECT_URL, 
    ("identify", "guilds", "email")
)  # scopes

# start
@router.on_event("startup")
async def on_startup():
    await discord.init()


@router.get("/discord-oauth")
async def discord_oauth(code: str):
    token, refresh_token = await discord.get_access_token(code)
    return {"access_token": token, "refresh_token": refresh_token}

@router.get("/discord_user/self", dependencies=[Depends(discord.requires_authorization)], response_model=User)
async def get_user(user: User = Depends(discord.user)):
    return user