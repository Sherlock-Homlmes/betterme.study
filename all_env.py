from json import load
import os
from dotenv import load_dotenv

load_dotenv()

environ = os.getenv("environ")
docs_url = os.getenv("docs_url")

database_url = os.environ.get('database_url')
