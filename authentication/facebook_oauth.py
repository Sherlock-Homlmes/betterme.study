# fastapi
from fastapi import Request
from fastapi.responses import JSONResponse

# oauth
from all_env import FACEBOOK_CLIENT_ID, FACEBOOK_CLIENT_SECRET, FACEBOOK_REDIRECT_URL
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix

# default
from dataclasses import dataclass

# local
from . import router

authorization_base_url = 'https://www.facebook.com/dialog/oauth'
token_url = 'https://graph.facebook.com/oauth/access_token'
facebook = OAuth2Session(FACEBOOK_CLIENT_ID,
                         redirect_uri=FACEBOOK_REDIRECT_URL)
facebook = facebook_compliance_fix(facebook)


@dataclass
class FaceBookOauth2:
  # OAuth endpoints given in the Facebook API documentation

  def get_oauth_url(self):
    authorization_url, state = facebook.authorization_url(
      authorization_base_url)
    return authorization_url

  def get_user_info(self, redirect_response: str):
    facebook.fetch_token(token_url,
                         client_secret=FACEBOOK_CLIENT_SECRET,
                         authorization_response=redirect_response)

    r = facebook.get('https://graph.facebook.com/me?')
    return r.json()


@router.get("/facebook-oauth")
async def facebook_oauth(request: Request):
  authorization_response = str(request.url)
  if not authorization_response.startswith('https'):
    authorization_response = authorization_response.replace('http', 'https')
  user = FaceBookOauth2().get_user_info(authorization_response)
  return JSONResponse(user, status_code=200)
