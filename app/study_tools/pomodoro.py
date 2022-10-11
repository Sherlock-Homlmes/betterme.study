from fastapi import Request
from fastapi.responses import JSONResponse
from base import app, TemplateResponse

@app.api_route('/pomodoro', methods=['GET','PUT','DELETE'])
async def pomodoro(request: Request):
    pass


