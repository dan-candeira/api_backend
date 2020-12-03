from db import db

from fastapi import HTTPException, status


async def validate_equipment(equipment_id: str):
    equipment = db.equipments.find_one({'_id': equipment_id})

    if equipment is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="an equipment with this id do not exists"
        )
    else:
        return equipment
