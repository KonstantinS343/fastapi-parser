from core.base_models import TimeStampedModel


class Twitch(TimeStampedModel):
    name: str


class Stream(Twitch):
    channel: str
    audience: str
