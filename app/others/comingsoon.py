from fastapi import Request
from base import app, TemplateResponse

@app.get("/comingsoon")
async def comingsoon(request: Request) -> TemplateResponse:
    data = {"request": request}
    return TemplateResponse("others/comingsoon.html", data)
