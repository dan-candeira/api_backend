from models.collect import Collect

from helpers.patient import validate_patient
from helpers.equipment import validate_equipment


async def validate_collect(collect: Collect):
    await validate_patient(collect.patient)
    await validate_equipment(collect.equipment)
    
    return collect