from datetime import datetime
from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, Field, UUID4, field_validator


class BookSchema(BaseModel):

    id: UUID4 = Field(default_factory=uuid4)
    title: str
    author: str
    publisher: Optional[str] = ''
    publish_date: datetime
    page_count: Optional[int] = 0
    language: str = Field(default='EN', max_length=2)

    @classmethod
    @field_validator('language')
    def validate_upper_case(cls, v: str) -> None:
        if not v.upper():
            raise
