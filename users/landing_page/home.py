from fastapi import Request, Response
from fastapi.responses import JSONResponse
from pydantic import ValidationError

import json
import io

from . import router
from base import TemplateResponse
from .schemas import ContactForm
from all_env import environ

import asyncio
async def test_background():
    for i in range(10):
        await asyncio.sleep(2)
        print(i)

@router.get("/")
async def test(request: Request) -> TemplateResponse:

    data = {"request": request, "environ": environ}
    return TemplateResponse("landing_page/home.html", data)

@router.get("/robots.txt")
async def robot_txt() -> Response:

    content = '''User-agent: *
Allow: /
Crawl-delay: 3
    '''

    return Response(content=content, media_type='text/plain')

@router.post("/contact-form")
async def contact_form(request: Request):
    form = await request.form()

    data = {}
    for key in form:
        data[key] = form[key]

    try:
        ContactForm(**data)
    except ValidationError:
        return JSONResponse({'message':'invalid email'}, status_code=400)


    email = data['email'].split('@')[0]
    with io.open(f'{email}.json', 'w', encoding='utf-8') as f1:
        json.dump(data, f1, ensure_ascii=False, indent=4)

    return JSONResponse({'message':'valid'},status_code=200)