from .settings import app
from .exeption_handle import *
from users import (
    landing_page, 
    study_tools,
    other_modules,
    others,   
)
import authentication

app.include_router(authentication.router)
app.include_router(landing_page.router)
app.include_router(study_tools.router)
app.include_router(other_modules.router)
app.include_router(others.router)
