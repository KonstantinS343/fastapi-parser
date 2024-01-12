import json

from tests.conftest import client  # noqa
from tests.twitch.conftest import test_twitch_data


class TestTwitchCategories:
    endpoint = '/twitch'

    async def test_parse(self, client, query):
        response = await client.post(url=self.endpoint + '/parse/categories', json=query)

        assert response.status_code == 201

    async def test_get_all_twitch_categories(self, client):
        response = await client.get(url=self.endpoint + '/categories')

        assert response.status_code == 200
        assert len(json.loads(response.content)['data']) > 0

    async def test_get_twitch_categories_by_id(self, client, twitch_categories_item):
        response = await client.get(url=self.endpoint + '/categories/' + f'{twitch_categories_item}')

        assert response.status_code == 200

        data = json.loads(response.content)['data']

        assert data['name'] == test_twitch_data['name']
