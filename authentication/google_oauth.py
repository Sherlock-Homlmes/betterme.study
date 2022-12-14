# fastapi
from fastapi import Request
from fastapi.responses import JSONResponse

# default
from dataclasses import dataclass

# oauth
from requests_oauthlib import OAuth2Session

# local
from all_env import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REDIRECT_URL
from . import router

scope = (
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",
)
oauth = OAuth2Session(
    client_id=GOOGLE_CLIENT_ID, redirect_uri=GOOGLE_REDIRECT_URL, scope=scope
)


@dataclass
class GoogleOauth2:
    def get_oauth_url(self):
        authorization_url, state = oauth.authorization_url(
            "https://accounts.google.com/o/oauth2/auth",
            access_type="offline",
            prompt="select_account",
        )
        return authorization_url

    def get_user_info(self, authorization_response):
        oauth.fetch_token(
            "https://accounts.google.com/o/oauth2/token",
            authorization_response=authorization_response,
            client_secret=GOOGLE_CLIENT_SECRET,
        )
        r = oauth.get("https://www.googleapis.com/oauth2/v1/userinfo")
        return r.json()


@router.get("/google-oauth")
async def google_oauth(request: Request):
    authorization_response = str(request.url)
    if not authorization_response.startswith("https"):
        authorization_response = authorization_response.replace("http", "https", 1)
    user = GoogleOauth2().get_user_info(authorization_response)
    return JSONResponse(user, status_code=200)
