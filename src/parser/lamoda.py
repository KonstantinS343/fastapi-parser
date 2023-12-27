from bs4 import BeautifulSoup
from httpx import AsyncClient


async def parse_lamoda_products(url: str) -> None:
    async with AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            cards = soup.find_all('div', class_='x-product-card__card')

            for card in cards:
                brand = card.find('div', class_='x-product-card-description__brand-name').text  # noqa
                name = card.find('div', class_='x-product-card-description__product-name').text  # noqa
                try:
                    price = card.find('span', class_='x-product-card-description__price-single').text
                except AttributeError:
                    price = card.find('span', class_='x-product-card-description__price-new').text
                price = float(price.replace(' р.', '').strip())
