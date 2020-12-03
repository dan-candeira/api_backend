from datetime import datetime
from typing import Optional, Field, List
from pydantic import BaseModel, Json

from helpers.objectid import PyObjectId
from datetime import datetime

from bson import ObjectId


class Sample(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    datetime_start: Optional[datetime] = datetime.utcnow()
    datetime_end: Optional[datetime]
    header: List[str]
    data_captured: Json
    collect: PyObjectId

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        schema_extra = {
            "example": {
                "header": "[string, string]",
                "data_captured": "{[value, value], [value, value]}",
                "collect": "string",
            }
        }