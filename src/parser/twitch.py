from httpx import AsyncClient, HTTPError

from config import settings


async def parse_twitch(type: str, query: str, limit: int = 20) -> None:
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
                data['data'].append(response['data'])
                limit -= first
                after = response['pagination']['cursor']
            else:
                break