from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional
from helpers.objectid import PyObjectId


class UserBase(BaseModel):
    id: Optional[PyObjectId] = Field(
        alias='_id')
    name: str
    username: str
    email: str
    disabled: Optional[bool] = None
    admin: Optional[bool] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


class User(UserBase):
    password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "username": "Bar",
                "email": "foobar@mail",
                "password": "1234;)"
            }
        }
