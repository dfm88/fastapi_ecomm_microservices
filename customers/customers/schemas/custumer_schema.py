from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class CustomerBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class CustomerCreate(CustomerBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class CustomerUpdate(CustomerBase):
    password: Optional[str] = None


class CustomerInDBBase(CustomerBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class CustomerOut(CustomerInDBBase):
    pass


# Additional properties stored in DB
class CustomerInDB(CustomerInDBBase):
    hashed_password: str
