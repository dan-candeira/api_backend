from fastapi import Depends, HTTPException, status

from datetime import timedelta, datetime
from typing import Optional


from jose import jwt, JWTError
from auth.config import oauth2_scheme

from db import db
from models.user import User
from models.token import TokenData

from helpers.password import verify_password

from settings import SECRET_KEY
ALGORITHM = 'HS256'


def get_user(username: str, db=db):
    user = None
    found_users = db.users.find({'username': username})
    for _user in found_users:
        user = User(**_user)
    return user


def authenticate_user(username: str, password: str, db=db):
    user = get_user(username)
    if not user:
        return False
    elif not verify_password(password, user.password):
        return False
    else:
        return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='invalid credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')

        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


def get_current_active_user(user: User = Depends(get_current_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='inactive user'
        )
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encode_jtw = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jtw


def is_current_active_user_admin(user: User = Depends(get_current_user)):
    if not user.admin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='you are not an admin :('
        )
    return user


def is_user_valid(user: User):
    user_alredy_registered = get_user(user.username)
    if user_alredy_registered is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='user alredy registered.'
        )
    return user