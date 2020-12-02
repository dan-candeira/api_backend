from pydantic import BaseModel, Field
from typing import  List, Optional
from datetime import  date

from helpers.objectid import PyObjectId
from bson import ObjectId


class Patient(BaseModel):
    id: Optional[PyObjectId] = Field(
        alias='_id')
    cpf: str
    first_name: str
    last_name: str
    birth_date: date
    email: Optional[str]
    phone: str
    address: str
    lat: Optional[str]
    long: Optional[str]
    collects: Optional[List[PyObjectId]]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        schema_extra = {
            "example": {
                "cpf": "00000000000",
                "first_name": "John",
                "last_name": "Doe",
                "birth_date": "1990-8-10",
                "email": "johndoe@mail.com",
                "phone": "+5500900000000",
                "address": "At a place"
            }
        }


