from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from models.user import User
from db import db

from helpers.password import get_password_hash
from helpers.user import get_current_active_user


router = APIRouter()


@router.get('/me', response_model=User)
async def get_current_user(user: User = Depends(get_current_active_user)):
    return user


@router.get('/', response_model=List[User])
async def list_users():
    users = []
    for user in db.users.find():
        users.append(User(**user))

    return users


@router.post('/', response_model=User)
async def create_user(user: User):
    if hasattr(user, 'id'):
        delattr(user, 'id')

    user.password = get_password_hash(user.password)
    _user = db.users.insert_one(user.dict(by_alias=True))
    user.id = _user.inserted_id

    return user
