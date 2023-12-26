from core.base_model import TimeStampedModel


class Games(TimeStampedModel):
    name: str
    audience: int


class Streamers(TimeStampedModel):
    name: str
    followers: int


class Stream(TimeStampedModel):
    channel: str
    name: str
    audience: str
