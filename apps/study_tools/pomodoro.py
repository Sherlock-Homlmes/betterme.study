from fastapi import Request
from fastapi.responses import JSONResponse

from . import router
from base import TemplateResponse

@router.api_route('/pomodoro', methods=['GET','PUT','DELETE'])
async def pomodoro(request: Request):
    pass


