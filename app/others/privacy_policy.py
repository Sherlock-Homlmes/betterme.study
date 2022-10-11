from fastapi import Request
from base import app, TemplateResponse

@app.get("/privacy-policy")
async def privacy_policy(request: Request) -> TemplateResponse:
    data = {"request": request}
    return TemplateResponse("others/privacy-policy.html", data)
