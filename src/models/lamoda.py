from core.base_model import TimeStampedModel


class Product(TimeStampedModel):
    name: str
    brand: str
    price: float
    article_number: str
