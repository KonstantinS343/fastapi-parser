from pydantic import BaseModel

from datetime import datetime


class TimeStampedModel(BaseModel):
    created_at: datetime


class Task(BaseModel):
    url: str
