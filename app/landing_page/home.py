from fastapi import Request
from fastapi.responses import JSONResponse, HTMLResponse

from pydantic import ValidationError

from base import app, TemplateResponse
from .models import ContactForm
from all_env import environ

@app.get("/")
async def test(request: Request) -> TemplateResponse:

    data = {"request": request, "environ": environ}
    return TemplateResponse("landing_page/home.html", data)

@app.get("/robots.txt")
async def robot_txt():

    content = '''
<pre style="word-wrap: break-word; white-space: pre-wrap;">
User-agent: *
Allow: /
Crawl-delay: 3 
</pre>
    '''

    return HTMLResponse(content)

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