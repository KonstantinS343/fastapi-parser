from core.base_models import TimeStampedModel


class Product(TimeStampedModel):
    name: str
    brand: str
    price: float
