from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr



class UserCreate(UserBase):
    password: str
    first_name: str
    last_name: str

class UserRead(UserBase):
    id: int
    full_name: str