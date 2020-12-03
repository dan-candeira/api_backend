from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from models.user import User
from models.collect import Collect

from db import db

from helpers.user import get_current_active_user, is_current_active_user_admin
from helpers.collect import is_collect_valid


router = APIRouter()


@router.get('/', response_model=List[Collect])
async def list_collects(user: User = Depends(get_current_active_user)):
    collects = []
    for collect in db.collects.find():
        collects.append(Collect(**collect))

    return collects


@router.post('/', response_model=Collect)
async def create_collect(collect: Collect = Depends(is_collect_valid), user: User = Depends(is_current_active_user_admin)):
    if hasattr(collect, 'id'):
        delattr(collect, 'id')

    _collect = db.collects.insert_one(collect.dict(by_alias=True))

    collect.id = _collect.inserted_id

    return collect
