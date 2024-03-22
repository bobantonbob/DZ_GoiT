from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class ContactSchema(BaseModel):
    first_name: str = Field(min_length=3, max_length=20)
    last_name: str = Field(min_length=3, max_length=20)
    email: str = Field(min_length=3, max_length=40)
    phone_number: str = Field(min_length=7, max_length=20)
    birthday: str = Field(max_length=20)
    extra_info: str = Field(min_length=3, max_length=250)


class ContactUpdateSchema(ContactSchema):
    pass


class ContactResponse(BaseModel):
    id: int = 1
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: str
    extra_info: str

    class Config:
        from_attributes = True
