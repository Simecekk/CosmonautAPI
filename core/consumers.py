import aiormq
from abc import ABC
from core import settings


class BaseConsumer(ABC):
    async def start_consumer(self):
        raise NotImplementedError

    async def callback(self, message):
        raise NotImplementedError


class RabbitMqConsumer(BaseConsumer):
    connection = None
    channel = None
    queue_name = ""

    async def start_consumer(self):
        self.connection = await aiormq.connect(settings.RABBITMQ_URL)
        self.channel = await self.connection.channel()
        await self.channel.queue_declare(queue=self.queue_name, durable=True)
        await self.channel.basic_consume(self.queue_name, consumer_callback=self.callback, no_ack=True)

    async def callback(self, message):
        raise NotImplementedError
