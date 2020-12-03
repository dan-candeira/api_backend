from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from models.user import User
from models.patient import Patient

from db import db
from helpers.user import get_current_active_user
from helpers.patient import get_patient_collects


router = APIRouter()


@router.get('/', response_model=List[Patient])
async def list_patients(user: User = Depends(get_current_active_user)):
    patients = []
    await get_patient_collects()
    for patient in db.patients.find():
        patients.append(Patient(**patient))

    return patients


@router.post('/', response_model=Patient)
async def create_patient(patient: Patient, user: User = Depends(get_current_active_user)):
    if hasattr(patient, 'id'):
        delattr(patient, 'id')

    year, month, day = str(patient.birth_date).split('-')
    date = datetime(int(year), int(month), int(day))
    patient.birth_date = date
    _patient = db.patients.insert_one(patient.dict(by_alias=True))

    patient.id = _patient.inserted_id

    return patient
