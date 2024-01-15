from bs4 import BeautifulSoup
from httpx import AsyncClient

from models.lamoda import Product
from core.mongo import get_mongo


async def parse_lamoda_products(url: str) -> None:
    """
    A function for parsing the lamoda website via a link.
    """

    mongo_service = await get_mongo()

    async with AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            cards = soup.find_all('div', class_='x-product-card__card')

            for card in cards:
                brand = card.find('div', class_='x-product-card-description__brand-name').text.strip()  # noqa
                name = card.find('div', class_='x-product-card-description__product-name').text.strip()  # noqa
                try:
                    price = card.find('span', class_='x-product-card-description__price-single').text
                except AttributeError:
                    price = card.find('span', class_='x-product-card-description__price-new').text
                price = float(price.replace(' р.', '').replace(' ', '').strip())

                product = Product(name=name, brand=brand, price=price)
                await mongo_service.insert('lamoda', product.model_dump())
