from fastapi import APIRouter
from models.user import User
from db import db

router = APIRouter()


@router.get('/')
async def list_users():
    users = []
    for user in db.users.find():
        users.append(User(**user))
    return {'users': users}


@router.post('/')
async def create_user(user: User):
    if hasattr(user, 'id'):
        delattr(user, 'id')

    ret = db.users.insert_one(user.dict(by_alias=True))
    user.id = ret.inserted_id

    return {'user': user}
