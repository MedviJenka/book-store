from datetime import datetime
from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, Field, UUID4, field_validator


class AuthSchema(BaseModel):
    ...
