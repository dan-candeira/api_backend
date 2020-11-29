from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional
from helpers.objectid import PyObjectId


class User(BaseModel):
    id: Optional[PyObjectId] = Field(
        alias='_id')
    name: str
    username: str
    email: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        schema_extra = {
            "example": {
                "name": "Foo",
                "username": "Bar",
                "email": "foobar@mail"
            }
        }
