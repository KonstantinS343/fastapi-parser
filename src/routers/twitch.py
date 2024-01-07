from fastapi import APIRouter, Response, status

from typing import List, Dict

from bson.objectid import ObjectId

from core.base_models import TaskQuery
from core.mongo import MongoService
from models.twitch import Twitch, Stream
from utils.kafka import Kafka


router = APIRouter(prefix='/twitch')
mongo = MongoService()


@router.post('/parse/categories')
async def parse_twitch_categories(task: TaskQuery) -> Response:
    """
    A function that implements a post request with the launch of a parser for twitch, that parse categories.
    """
    kafka = Kafka()
    await kafka.send_one('parse', 'parser.twitch parse_twitch categories ' + task.query + ' ' + task.limit)
    return Response(content='Parsing task created successfully', status_code=status.HTTP_201_CREATED, media_type='text/plain')


@router.post('/parse/channels')
async def parse_twitch_channels(task: TaskQuery) -> Response:
    """
    A function that implements a post request with the launch of a parser for twitch, that parse channels.
    """
    kafka = Kafka()
    await kafka.send_one('parse', 'parser.twitch parse_twitch channels ' + task.query + ' ' + task.limit)
    return Response(content='Parsing task created successfully', status_code=status.HTTP_201_CREATED, media_type='text/plain')


@router.post('/parse/stream')
async def parse_twitch_stream(task: TaskQuery) -> Response:
    """
    A function that implements a post request with the launch of a parser for twitch, that parse stream.
    """
    kafka = Kafka()
    await kafka.send_one('parse', 'parser.twitch parse_twitch stream ' + task.query + ' ' + task.limit)
    return Response(content='Parsing task created successfully', status_code=status.HTTP_201_CREATED, media_type='text/plain')


@router.get('/categories', response_model=Dict[str, List[Twitch]])
async def categories() -> Dict[str, List[Twitch]]:
    """
    A function that implements a get request, that returns all data about twitch categories from the database.
    """
    cursor = await mongo.get(collection='twitch_categories')
    products = []
    async for document in cursor:
        document['_id'] = str(document['_id'])
        products.append(document)

    return {'data': products}


@router.get('/categories/{category_id}', response_model=Dict[str, Twitch])
async def get_category(category_id: str) -> Dict[str, Twitch]:
    """
    A function that implements a get request, that returns information about a specific twitch channel from the database.
    """
    cursor = await mongo.get(collection='twitch_categories', query={"_id": ObjectId(category_id)})
    products = await cursor.next()

    return {'data': products}


@router.get('/channels', response_model=Dict[str, List[Twitch]])
async def channels() -> Dict[str, List[Twitch]]:
    """
    A function that implements a get request, that returns all data about twitch channels from the database.
    """
    cursor = await mongo.get(collection='twitch_channels')
    products = []
    async for document in cursor:
        document['_id'] = str(document['_id'])
        products.append(document)

    return {'data': products}


@router.get('/channels/{channel_id}', response_model=Dict[str, Twitch])
async def get_channel(channel_id: str) -> Dict[str, Twitch]:
    """
    A function that implements a get request, that returns information about a specific twitch category from the database.
    """
    cursor = await mongo.get(collection='twitch_channels', query={"_id": ObjectId(channel_id)})
    products = await cursor.next()

    return {'data': products}


@router.get('/streams', response_model=Dict[str, List[Stream]])
async def streams() -> Dict[str, List[Stream]]:
    """
    A function that implements a get request, that returns all data about twitch stream from the database.
    """
    cursor = await mongo.get(collection='twitch_stream')
    products = []
    async for document in cursor:
        document['_id'] = str(document['_id'])
        products.append(document)

    return {'data': products}


@router.get('/streams/{stream_id}', response_model=Dict[str, Twitch])
async def get_stream(stream_id: str) -> Dict[str, Twitch]:
    """
    A function that implements a get request, that returns information about a specific twitch stream from the database.
    """
    cursor = await mongo.get(collection='twitch_stream', query={"_id": ObjectId(stream_id)})
    products = await cursor.next()

    return {'data': products}
