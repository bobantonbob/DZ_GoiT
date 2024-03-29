import pydantic

class ContactResponseSchema(pydantic.BaseModel):
    id: int
    first_name: str
    last_name: str
    email: pydantic.EmailStr
    phone_number: str
    birthday: str
    extra_info: str

