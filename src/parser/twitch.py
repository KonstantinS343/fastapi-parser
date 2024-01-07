from httpx import AsyncClient, HTTPError

from config import settings
from core.mongo import MongoService
from models.twitch import Twitch, Stream


async def parse_twitch(type: str, query: str, lim: str) -> None:
    """
    A function for twitch parsing using the Twitch API, for categories, streamers and stream.
    """
    limit = int(lim)
    mongo_service = MongoService()

    data = {'client_id': settings.twitch_settings.client_id, 'client_secret': settings.twitch_settings.client_secret, 'grant_type': 'client_credentials'}

    params = {
        'categories': ('https://api.twitch.tv/helix/search/categories', 'query'),
        'channels': ('https://api.twitch.tv/helix/search/channels', 'query'),
        'stream': ('https://api.twitch.tv/helix/streams', 'user_login'),
    }

    async with AsyncClient() as client:
        try:
            response = await client.post('https://id.twitch.tv/oauth2/token', data=data)
            response.raise_for_status()
        except HTTPError:
            print('Error')

        bearer = response.json()['access_token']

        headers = {
            'Authorization': f'Bearer {bearer}',
            'Client-Id': settings.twitch_settings.client_id,
        }
        url, search_str = params[type]
        after = ''
        data = {'data': []}
        while limit:
            first = 100 if limit > 100 else limit
            response = await client.get(url, headers=headers, params={search_str: query, 'first': first, 'after': after})
            if response.status_code == 200:
                response = response.json()
                data['data'].extend(response['data'])
                limit -= first
                after = response['pagination']['cursor']
                if type == 'stream':
                    break
            else:
                break
        for item in data['data']:
            if type == 'categories':
                obj = Twitch(name=item['name'])
            elif type == 'channels':
                obj = Twitch(name=item['display_name'])
            elif type == 'stream':
                obj = Stream(channel=item['user_name'], audience=item['viewer_count'])
            await mongo_service.insert('twitch_' + type, obj.model_dump())
