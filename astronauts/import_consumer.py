import json
from copy import deepcopy
from datetime import datetime, timedelta

from astronauts.models import Astronaut
from astronauts.types import AstronautInputType
from core import settings
from core.consumers import RabbitMqConsumer
from core.settings import database


class AstronautImportConsumer(RabbitMqConsumer):
    queue_name = settings.RABBITMQ_IMPORT_ASTRONAUTS_QUEUE

    BATCH_SIZE: int = 10000
    TIME_INTERVAL: timedelta = timedelta(seconds=5)

    records: list[AstronautInputType] = []
    last_insert_time: datetime = datetime.now()

    async def callback(self, message):
        data = AstronautInputType(**json.loads(message.body.decode()))

        self.records.append(data)

        if len(self.records) >= self.BATCH_SIZE or datetime.now() - self.last_insert_time >= self.TIME_INTERVAL:
            records = deepcopy(self.records[:self.BATCH_SIZE])
            self.last_insert_time = datetime.now()
            self.records = []
            await self.insert_records(records)

    @staticmethod
    async def insert_records(records: list[AstronautInputType]):
        query = Astronaut.insert().values()
        await database.execute_many(query=query, values=[record.model_dump() for record in records])
        print(f"Astronauts imported: {datetime.now()}, Batch size: {len(records)}")
