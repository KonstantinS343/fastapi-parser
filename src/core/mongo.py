from motor.motor_asyncio import AsyncIOMotorClient

from datetime import datetime

from config import settings


class MongoService:
    def __init__(self) -> None:
        self.client = AsyncIOMotorClient(f'mongodb://{settings.mongo_settings.host}:{settings.mongo_settings.port}')
        self.db = self.client[settings.mongo_settings.database]

    async def insert(self, collection, document):
        collection = self.db[collection]
        document['created_at'] = datetime.now().time()
        await collection.insert_one(document)
