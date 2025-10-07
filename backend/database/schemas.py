from typing import Union
from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    email: Union[EmailStr, str] = Field(default='', description='user initial email')
    is_created: bool = False
