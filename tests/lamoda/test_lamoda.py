import json

from tests.conftest import client  # noqa
from tests.lamoda.conftest import test_product_data


class TestLamoda:
    endpoint = '/lamoda'

    async def test_parse(self, client, lamoda):
        response = await client.post(url=self.endpoint + '/parse', json=lamoda)

        assert response.status_code == 201

    async def test_get_all_products(self, client):
        response = await client.get(url=self.endpoint + '/products')

        assert response.status_code == 200
        assert len(json.loads(response.content)['data']) > 0

    async def test_get_product_by_id(self, client, lamoda_product):
        response = await client.get(url=self.endpoint + '/product/' + f'{lamoda_product}')

        assert response.status_code == 200

        data = json.loads(response.content)['data']

        assert data['brand'] == test_product_data['brand']
        assert data['name'] == test_product_data['name']
        assert data['price'] == test_product_data['price']
