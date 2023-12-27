from pydantic import BaseModel

from datetime import datetime


class TimeStampedModel(BaseModel):
    created_at: datetime


class TaskURL(BaseModel):
    url: str


class TaskQuery(BaseModel):
    query: str
