import asyncio

from kafka import Kafka

if __name__ == '__main__':
    kafka = Kafka()

    async def consume() -> None:
        while True:
            await kafka.consume('parse')

    asyncio.run(consume())
