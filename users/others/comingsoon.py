from fastapi import Request

from . import router
from base import TemplateResponse

@router.get("/comingsoon")
async def comingsoon(request: Request) -> TemplateResponse:
    data = {"request": request}
    return TemplateResponse("others/comingsoon.html", data)
