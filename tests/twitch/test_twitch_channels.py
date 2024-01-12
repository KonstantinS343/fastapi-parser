import json

from tests.conftest import client  # noqa
from tests.twitch.conftest import test_twitch_data


class TestTwitchChannels:
    endpoint = '/twitch'

    async def test_parse(self, client, query):
        response = await client.post(url=self.endpoint + '/parse/channels', json=query)

        assert response.status_code == 201

    async def test_get_all_twitch_channels(self, client):
        response = await client.get(url=self.endpoint + '/channels')

        assert response.status_code == 200
        assert len(json.loads(response.content)['data']) > 0

    async def test_get_twitch_channels_by_id(self, client, twitch_channels_item):
        response = await client.get(url=self.endpoint + '/channels/' + f'{twitch_channels_item}')

        assert response.status_code == 200

        data = json.loads(response.content)['data']

        assert data['name'] == test_twitch_data['name']
