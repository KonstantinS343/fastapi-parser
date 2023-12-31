from core.base_models import TimeStampedModel


class Twitch(TimeStampedModel):
    name: str


class Stream(TimeStampedModel):
    channel: str
    audience: int
