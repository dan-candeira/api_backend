from models.patient import Patient
from models.collect import Collect
from db import db

async def get_patient_collects():
    for patient in db.patients.find():
        collects = []
        for collect in db.collects.find({'patient': patient['_id']}):
            collects.append(Collect(**collect))
        db.patient.update({'_id': patient['_id']}, {'$set': {'collects': collects}})
    