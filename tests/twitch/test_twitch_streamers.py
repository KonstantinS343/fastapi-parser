import json

from tests.conftest import client  # noqa
from tests.twitch.conftest import test_twitch_stream_data


class TestTwitchStreamers:
    endpoint = '/twitch'

    async def test_parse(self, client, query_stream):
        response = await client.post(url=self.endpoint + '/parse/stream', json=query_stream)

        assert response.status_code == 201

    async def test_get_all_twitch_streamers(self, client):
        response = await client.get(url=self.endpoint + '/streams')

        assert response.status_code == 200

    async def test_get_twitch_streamers_by_id(self, client, twitch_streamers_item):
        response = await client.get(url=self.endpoint + '/streams/' + f'{twitch_streamers_item}')

        assert response.status_code == 200

        data = json.loads(response.content)['data']

        assert data['channel'] == test_twitch_stream_data['channel']
        assert data['audience'] == test_twitch_stream_data['audience']
