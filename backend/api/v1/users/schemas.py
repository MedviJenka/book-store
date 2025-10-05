from datetime import datetime
from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, Field, UUID4, EmailStr


class UserSchema(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    username: Optional[str] = Field(default=f'user-{uuid4()}')
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    email: EmailStr
    is_varified: bool = False
    created_at: datetime
    updated_at: datetime
