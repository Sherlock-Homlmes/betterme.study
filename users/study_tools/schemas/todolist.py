# fastapi
from pydantic import BaseModel, Field, validator
# default
import datetime
# local
from other_modules.time_modules import vn_now


class TodoList(BaseModel):
    # id: int
    title: str
    description: str = Field(default='')
    status: str = Field(default='TO-DO')
    necessary: str = Field(default='NORMAL')
    difficult: int = Field(default=3, ge=1, le=5)

    created_at: datetime.datetime = Field(default=vn_now())
    updated_at: datetime.datetime = Field(default=vn_now())
    user_id: int

    class Config:
        extra = 'forbid'

    @validator('status')
    def status_in_list(cls, v):
        if v not in ['TO-DO', 'DOING', 'DONE']:
            raise ValueError('invalid status')
        return v

    @validator('necessary')
    def necessary_in_list(cls, v):
        if v not in ['NOT IMPORTANT', 'NORMAL', 'QUITE IMPORTANT', 'VERY IMPORTANT']:
            raise ValueError('invalid neccessary')
        return v
