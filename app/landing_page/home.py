from fastapi import Request
from fastapi.responses import JSONResponse

from pydantic import ValidationError

from base import app, TemplateResponse
from .models import ContactForm

@app.get("/")
async def test(request: Request) -> TemplateResponse:

    data = {"request": request}
    return TemplateResponse("landing_page/home.html", data)

@app.get("/robot.txt")
async def robot_txt():

    return 0

@app.post("/contact-form")
async def contact_form(request: Request):
    form = await request.form()

    data = {}
    for key in form:
        data[key] = form[key]

    try:
        ContactForm(**data)
    except ValidationError:
        return JSONResponse({'message':'invalid email'}, status_code=400)

    return JSONResponse({'message':'valid'},status_code=200)