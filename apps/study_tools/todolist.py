from fastapi import Request
from fastapi.responses import JSONResponse

from . import router
from base import TemplateResponse

@router.api_route('/todolist', methods=['GET','PUT','DELETE'])
async def todolist(request: Request):
    pass


