# fastapi
from fastapi import Depends

#discord
from fastapi_discord import User, DiscordOAuthClient

# default
import aiohttp
#local
from . import router
from all_env import self_url
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
    headersList = {
        'Authorization': f'Bearer {token}'
    }
    async with aiohttp.ClientSession() as session:
        res = await session.get(url=f'{self_url}/auth/discord/user/self', headers=headersList)
    return await res.json()

@router.get("/discord/user/self", dependencies=[Depends(discord.requires_authorization)], response_model=User)
async def get_user(user: User = Depends(discord.user)):
    return user