from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)

from .discord_oauth import *