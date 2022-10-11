# default
import uvicorn

# custom
from all_env import environ
from app import *
from base import app

if __name__ == '__main__':
  uvicorn.run("main:app",host='0.0.0.0', port=8008, reload=True, workers=4)