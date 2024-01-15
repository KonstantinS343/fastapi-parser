from pydantic import BaseModel, field_validator

from typing import Optional

from datetime import datetime


class TimeStampedModel(BaseModel):
    created_at: Optional[datetime] = None

    @field_validator('created_at', mode="before")
    def validate_created_at_field(cls, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
            except ValueError:
                raise ValueError('Invalid datetime format.')
        return value


class TaskURL(BaseModel):
    url: str


class TaskQuery(BaseModel):
    query: str
    limit: str = '20'
