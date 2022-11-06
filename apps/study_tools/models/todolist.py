# from uuid import uuid4, UUID
from pydantic import BaseModel, Field, validator

class TodoList(BaseModel):
    id: int = Field(default=1)
    
    title: str
    description: str = Field(default='')
    status: str = Field(default='TO-DO')
    necessary: str = Field(default='NORMAL')
    difficult: int = Field(default=3, ge=1, le=5)

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
