from motor.motor_asyncio import AsyncIOMotorClient

from datetime import datetime

from config import settings


class MongoService:
    def __init__(self) -> None:
        self.client = AsyncIOMotorClient(f'mongodb://{settings.mongo_settings.host}:{settings.mongo_settings.port}')
        self.db = self.client[settings.mongo_settings.db]

    async def insert(self, collection, document):
        collection = self.db[collection]
        document['created_at'] = str(datetime.now())
        await collection.insert_one(document)

    async def get(self, collection, query={}):
        collection = self.db[collection]
        return collection.find(query)
