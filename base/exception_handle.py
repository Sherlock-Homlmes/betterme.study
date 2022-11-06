from .settings import app
from fastapi.responses import JSONResponse
from pydantic.error_wrappers import ValidationError


@app.exception_handler(ValidationError)
async def validation_error_handler(_, e: ValidationError):
    return JSONResponse({"detail": e.errors()}, status_code=400)
