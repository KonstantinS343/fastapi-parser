from motor.motor_asyncio import AsyncIOMotorClient

from datetime import datetime

from config import settings


class MongoService:
    def __init__(self, db=settings.mongo_settings.db) -> None:
        self.client = AsyncIOMotorClient(f'mongodb://{settings.mongo_settings.host}:{settings.mongo_settings.port}')
        self.db = self.client[db]

    async def insert(self, collection, document):
        collection = self.db[collection]
        document['created_at'] = str(datetime.now())
        result = await collection.insert_one(document)
        return result.inserted_id

    async def get(self, collection, query={}):
        collection = self.db[collection]
        return collection.find(query)


async def get_mongo():
    return MongoService()
