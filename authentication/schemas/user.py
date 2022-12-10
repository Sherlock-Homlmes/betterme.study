# fastapi
from pydantic import BaseModel, EmailStr, Field

# default
import datetime

# local
from other_modules.time_modules import vn_now

from all_env import bot_api

class Users(BaseModel):
    email: EmailStr = Field()
    password: str = Field(default=None)
    avatar: str = Field(default=None)


class UsersInfo(BaseModel):
    id: int
    email: EmailStr = Field()
    avatar: str = Field(default=None)

    discord_id: str = Field(default=None)
    discord_email: EmailStr = Field(default=None)
    google_id: str = Field(default=None)
    google_email: EmailStr = Field(default=None)
    facebook_id: str = Field(default=None)
    facebook_email: EmailStr = Field(default=None)

    joined_at: datetime.datetime = Field(default=vn_now())
    last_logged_in_at: datetime.datetime = Field(default=vn_now())
