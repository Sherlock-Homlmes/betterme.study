#  fastapi
from fastapi import HTTPException, Security, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

# default
import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

# local
from . import router
from .schemas import Users

class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = 'SECRET'

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, user_id):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=8640),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm='HS256'
        )

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Signature has expired')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail='Invalid token')

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)

auth_handler = AuthHandler()
users_list = []

@router.post('/register', status_code=201)
def register(users: Users):
    if any(x['email'] == users.email for x in users_list):
        raise HTTPException(status_code=400, detail='email is taken')
    hashed_password = auth_handler.get_password_hash(users.password)
    users_list.append({
        'email': users.email,
        'password': hashed_password    
    })
    return users_list


@router.post('/login')
def login(users: Users):
    user = [x for x in users_list if x['email'] == users.email]
    if (user == []) or (not auth_handler.verify_password(users.password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid email and/or password')
    user = user[0]
    token = auth_handler.encode_token(user['email'])
    return { 'token': token }

@router.get('/auth/self', dependencies=[Depends(auth_handler.auth_wrapper)])
def protected(user: Users = Depends(auth_handler.auth_wrapper)):
    return user