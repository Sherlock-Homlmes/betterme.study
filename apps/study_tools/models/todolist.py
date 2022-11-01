# from uuid import uuid4, UUID
from pydantic import BaseModel, Field, validator
import datetime, pytz

def vn_time():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("Asia/Ho_Chi_Minh"))
    today =  datetime.datetime(pst_now.year , pst_now.month , pst_now.day, pst_now.hour, pst_now.minute)
    
    return today

class TodoList(BaseModel):
    # id: UUID = Field(default_factory=uuid4)
    
    title: str
    description: str = Field(default='')
    status: str = Field(default='TO-DO')
    necessary: str = Field(default='NORMAL')
    difficult: int = Field(default=3, ge=1, le=5)

    created_at: datetime.datetime = Field(default=vn_time())
    updated_at: datetime.datetime = Field(default=vn_time())
    user_id: int

    class Config:
        extra = 'forbid'

    @validator('status')
    def status_in_list(cls, v):
        if v not in ['TO-DO','DOING','DONE']:
            raise ValueError('invalid status')
        return v

    @validator('necessary')
    def necessary_in_list(cls, v):
        if v not in ['NOT IMPORTANT','NORMAL','QUITE IMPORTANT','VERY IMPORTANT']:
            raise ValueError('invalid neccessary')
        return v