from fastapi import APIRouter

router = APIRouter(
    tags=["Landing page"],
    responses={404: {"description": "Not found"}},
)

from .home import *