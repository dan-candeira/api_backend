from pydantic import BaseModel, Field
from typing import List, Optional

from helpers.objectid import PyObjectId
from bson import ObjectId


class Equipment(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    mac_address: str
    name: str
    description: str
    samppling_frequency: str
    available: bool = True
    sensors: Optional[List[PyObjectId]]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        schema_extra = {
            "_id": "string",
            "mac_address": "string",
            "name": "string",
            "description": "string",
            "samppling_frequency": "string",
            "available": "false"
        }
