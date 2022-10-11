from fastapi import Request
from fastapi.responses import (
    HTMLResponse,
    RedirectResponse, 
    JSONResponse,
    FileResponse
)
from base import app, TemplateResponse

@app.get("/exam-cert")
async def exam_cert():
    return FileResponse('static/images/betterme-certificate.png')