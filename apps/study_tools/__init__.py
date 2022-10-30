from fastapi import APIRouter

router = APIRouter(
    tags=["Study tools"],
    responses={404: {"description": "Not found"}},
)

from .todolist import *
from .pomodoro import *
from .quotes import *