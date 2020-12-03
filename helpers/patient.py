from models.collect import Collect
from db import db


from fastapi import HTTPException, status


async def get_patient_collects():
    for patient in db.patients.find():
        collects = []
        for collect in db.collects.find({'patient': patient['_id']}):
            collects.append(Collect(**collect))
        db.patient.update({'_id': patient['_id']}, {'$set': {'collects': collects}})


async def validate_patient(patient_id: str):
    patient = db.patients.find_one({'_id': patient_id})

    if patient is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="a patient with this id do not exists"
        )
    else:
        return patient