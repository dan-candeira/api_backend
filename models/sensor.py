from pydantic import BaseModel, Field
from typing import Optional

from helpers.objectid import PyObjectId
from bson import ObjectId


class Sensor(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    model: str
    measuring_dimention: str
    description: str
    equipment: PyObjectId

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        schema_extra = {
            "model": "string",
            "measuring_dimention": "string",
            "description": "string",
            "description": "string",
            "equipment": "string"
        }