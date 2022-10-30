from fastapi import APIRouter

router = APIRouter(
    tags=["Other"],
    responses={404: {"description": "Not found"}},
)

from .error_404 import *
from .comingsoon import *
from .loading import *
from .privacy_policy import *