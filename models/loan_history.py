from pydantic import BaseModel, Field
from typing import Optional

from datetime import datetime

from helpers.objectid import PyObjectId
from bson import ObjectId



class LoanHistory(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    equipment: PyObjectId
    patient: PyObjectId
    loan_datetime: datetime
    devolution_datetime: Optional[datetime]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        schema_extra = {
            "example": {
                "equipment": "string",
                "patient": "string",
                "loan_datetime": "2020-12-03 14:25:06.365341"
            }
        }
