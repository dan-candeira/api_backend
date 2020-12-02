from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from models.user import User
from models.equipment import Equipment

from db import db

from helpers.user import get_current_active_user, is_current_active_user_admin


router = APIRouter()


@router.get('/', response_model=List[Equipment])
async def list_equipments(user: User = Depends(get_current_active_user)):
    equipments = []
    for equipment in db.equipments.find():
        equipments.append(equipment(**equipment))

    return equipments


@router.post('/', response_model=Equipment)
async def create_equipment(equipment: Equipment, user: User = Depends(is_current_active_user_admin)):
    if hasattr(equipment, 'id'):
        delattr(equipment, 'id')

    _equipment = db.equipments.insert_one(equipment.dict(by_alias=True))

    equipment.id = _equipment.inserted_id

    return equipment
