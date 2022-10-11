from lib2to3.pgen2.token import OP
from pydantic import BaseModel, EmailStr
from typing import Union, Optional
from datetime import datetime

class User(BaseModel):
    gender_text = {'Nam', 'Nữ'}
    age_range = {'Cấp 1', 'Cấp 2', 'Cấp 3', 'Đại học-Cao đẳng', 'Thạc sĩ-Tiến sĩ', 'Tốt nghiệp-đi làm'}

    user_id: int
    email: EmailStr
    password: str
    joined_at: datetime
    accounts: list

    gender: Optional[str]
    age: Optional[Union[int, str]]
    

    username: str
    avatar_url: Optional[str]