from fastapi import APIRouter, Response, status

from typing import List, Dict

from bson.objectid import ObjectId

from core.base_models import TaskURL
from core.mongo import MongoService
from models.lamoda import Product
from utils.kafka import Kafka
from utils.redis import get_cache, set_cache, clear_cache
from utils.services import parse_redis_result


router = APIRouter(prefix='/lamoda')
mongo = MongoService()


@router.post('/parse')
async def parse_lamoda(task: TaskURL) -> Response:
    """
    A function that implements a post request with the launch of a parser for lamoda.
    """
    kafka = Kafka()
    await kafka.send_one('parse', 'parser.lamoda parse_lamoda_products ' + task.url)
    await clear_cache('lamoda', 'lamoda')
    return Response(content='Parsing task created successfully', status_code=status.HTTP_201_CREATED, media_type='text/plain')


@router.get('/products', response_model=Dict[str, List[Product]])
async def products() -> Dict[str, List[Product]]:
    """
    A function that implements a get request, that returns all data about lamoda from the database.
    """
    products = await get_cache('lamoda', 'lamoda')
    if not products:
        cursor = await mongo.get(collection='lamoda')
        products = []
        async for document in cursor:
            document['_id'] = str(document['_id'])
            products.append(document)
        await set_cache('lamoda', products, 'lamoda')
    return {'data': await parse_redis_result(products)}


@router.get('/product/{product_id}', response_model=Dict[str, Product])
async def get_product(product_id: str) -> Dict[str, Product]:
    """
    A function that implements a get request, that returns information about a specific lamoda product from the database.
    """
    cursor = await mongo.get(collection='lamoda', query={"_id": ObjectId(product_id)})
    products = await cursor.next()

    return {'data': products}
