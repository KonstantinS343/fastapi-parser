from pydantic import BaseModel

from typing import Optional

from datetime import datetime


class TimeStampedModel(BaseModel):
    created_at: Optional[datetime] = None


class TaskURL(BaseModel):
    url: str


class TaskQuery(BaseModel):
    query: str
