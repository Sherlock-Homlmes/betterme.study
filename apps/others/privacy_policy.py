from fastapi import Request

from . import router
from base import TemplateResponse

@router.get("/privacy-policy")
async def privacy_policy(request: Request) -> TemplateResponse:
    data = {"request": request}
    return TemplateResponse("others/privacy-policy.html", data)
