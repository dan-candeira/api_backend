from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from models.user import User
from db import db


router = APIRouter()


# @router.get('/me', response_model=User)
# async def get_current_user(user: User = Depends(get_current_active_user)):
#     users = []
#     for user in db.users.find():
#         users.append(User(**user))
#     return {'users': users}


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

    ret = db.users.insert_one(user.dict(by_alias=True))
    user.id = ret.inserted_id

    return user
