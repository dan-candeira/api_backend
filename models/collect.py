from pydantic import BaseModel, Field
from typing import Optional, List

from helpers.objectid import PyObjectId
from bson import ObjectId

from datetime import datetime

from models.patient import Patient
from models.equipment import Equipment


class Collect(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    datetime_start: datetime = datetime.utcnow()
    datetime_end: Optional[datetime]
    samples: Optional[List[PyObjectId]]
    patient: PyObjectId
    equipment: PyObjectId

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
