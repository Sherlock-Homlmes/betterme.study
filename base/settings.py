from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from all_env import docs_url

# base setting
app = FastAPI(docs_url=f"/{docs_url}", redoc_url=None)
templates = Jinja2Templates(directory="templates")
TemplateResponse = templates.TemplateResponse
app.mount("/static", StaticFiles(directory="./static"), name="static")
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

