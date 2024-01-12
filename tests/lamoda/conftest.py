import pytest

from src.core.mongo import get_mongo


test_product_data = {'name': 'Test', 'brand': 'Test', 'price': 0.0}


@pytest.fixture
async def lamoda():
    return {'url': 'https://www.lamoda.by/c/2937/clothes-clothes-big-size/'}


@pytest.fixture
async def lamoda_product():
    mongo = await get_mongo()
    inserted_id = await mongo.insert('lamoda', test_product_data)

    return inserted_id
