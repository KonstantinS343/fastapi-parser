from fastapi import APIRouter, Response, status

from typing import List, Dict

from bson.objectid import ObjectId

from core.base_models import TaskURL
from core.mongo import MongoService
from parser.lamoda import parse_lamoda_products
from models.lamoda import Product


router = APIRouter(prefix='/lamoda')
mongo = MongoService()


@router.post('/parse')
async def parse_lamoda(task: TaskURL) -> Response:
    """
    A function that implements a post request with the launch of a parser for lamoda.
    """
    await parse_lamoda_products(task.url)
    return Response(content='Parsing task created successfully', status_code=status.HTTP_201_CREATED, media_type='text/plain')


@router.get('/products', response_model=Dict[str, List[Product]])
async def products() -> Dict[str, List[Product]]:
    """
    A function that implements a get request, that returns all data about lamoda from the database.
    """
    cursor = await mongo.get(collection='lamoda')
    products = []
    async for document in cursor:
        document['_id'] = str(document['_id'])
        products.append(document)

    return {'data': products}


@router.get('/product/{product_id}', response_model=Dict[str, Product])
async def get_product(product_id: str) -> Dict[str, Product]:
    """
    A function that implements a get request, that returns information about a specific lamoda product from the database.
    """
    cursor = await mongo.get(collection='lamoda', query={"_id": ObjectId(product_id)})
    products = await cursor.next()

    return {'data': products}
