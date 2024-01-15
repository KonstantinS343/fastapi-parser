import pytest

from src.core.mongo import get_mongo


test_twitch_data = {'name': 'Test'}

test_twitch_stream_data = {'channel': 'Test', 'audience': 0}


@pytest.fixture
async def query():
    return {
        'query': 'a',
    }


@pytest.fixture
async def query_stream():
    return {
        'query': 'zubarefff',
    }


@pytest.fixture
async def twitch_categories_item():
    mongo = await get_mongo()
    inserted_id = await mongo.insert('twitch_categories', test_twitch_data)

    return inserted_id


@pytest.fixture
async def twitch_channels_item():
    mongo = await get_mongo()
    inserted_id = await mongo.insert('twitch_channels', test_twitch_data)

    return inserted_id


@pytest.fixture
async def twitch_streamers_item():
    mongo = await get_mongo()
    inserted_id = await mongo.insert('twitch_stream', test_twitch_stream_data)

    return inserted_id
