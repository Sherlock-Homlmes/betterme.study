from json import load
import os
from dotenv import load_dotenv

load_dotenv()

#environ
environ = os.getenv("environ")

#fastapi
docs_url = os.getenv("docs_url")

#mongodb
database_url = os.environ.get('database_url')

#discord_oauth
CLIENT_ID = os.environ.get('CLIENT_ID')
TOKEN = os.environ.get('TOKEN')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URL = os.environ.get('REDIRECT_URL')

#bot api
bot_api = os.environ.get('bot_api')