from aiokafka import AIOKafkaConsumer, AIOKafkaProducer

from importlib import import_module

from config import settings


class Kafka:
    def __init__(self) -> None:
        self.bootstrap_servers = settings.kafka_settings.bootstrap_servers

    async def process_message(self, message: bytes):
        arguments = message.decode().split()
        module_name, function_name, task = arguments if len(arguments) == 3 else (arguments[0], arguments[1], arguments[2:])

        module = import_module(module_name)  # type: ignore
        function = getattr(module, function_name)  # type: ignore
        print(task)
        if isinstance(task, str):
            await function(task)
        else:
            await function(*task)

    async def send_one(self, topic: str, message: str):
        producer = AIOKafkaProducer(bootstrap_servers=self.bootstrap_servers)
        await producer.start()

        try:
            await producer.send_and_wait(topic=topic, value=message.encode())
        except Exception as e:
            print(e)
        finally:
            await producer.stop()

    async def consume(self, topic: str):
        consumer = AIOKafkaConsumer(topic, bootstrap_servers=self.bootstrap_servers)
        await consumer.start()

        try:
            async for i in consumer:
                await self.process_message(i.value)
        except Exception as e:
            print(e)
        finally:
            await consumer.stop()
