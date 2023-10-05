import asyncio
import json
import random
import uuid

import aiormq

from core import settings


async def send_message(message, queue_name, channel):

    await channel.queue_declare(queue_name, durable=True)

    await channel.basic_publish(
        message.encode("utf-8"),
        exchange='',
        routing_key=queue_name
    )


async def main():
    queue_name = settings.RABBITMQ_IMPORT_ASTRONAUTS_QUEUE
    message_count = 100000

    connection = await aiormq.connect("amqp://guest:guest@localhost/")
    channel = await connection.channel()

    tasks = [send_message(
        json.dumps(
            {"name": f"astronaut-{uuid.uuid4().hex[:5]}", "age": random.randint(20, 100)},
        ),
        queue_name,
        channel
    ) for _ in range(message_count)]
    await asyncio.gather(*tasks)

    await connection.close()

if __name__ == '__main__':
    asyncio.run(main())
