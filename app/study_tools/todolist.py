from fastapi import Request
from fastapi.responses import JSONResponse
from base import app, TemplateResponse

@app.api_route('/todolist', methods=['GET','PUT','DELETE'])
async def todolist(request: Request):
    pass


