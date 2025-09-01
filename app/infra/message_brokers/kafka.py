from dataclasses import dataclass
from typing import AsyncIterator

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import orjson

from infra.message_brokers.base import BaseMessageBroker

@dataclass
class KafkaMessageBroker(BaseMessageBroker):
    producer: AIOKafkaProducer
    consumer: AIOKafkaConsumer

    async def send_message(self,key: bytes, topic: str, value: bytes, headers: list[tuple]):
        await self.producer.send_and_wait(topic=topic, key=key, value=value, headers=headers)

    async def start_consuming(self, topic: str) -> AsyncIterator[dict]:
        self.consumer.subscribe(topics=[topic])
        
        async for message in self.consumer:
            yield orjson.loads(message.value)

    async def start(self):
        await self.producer.start()
        await self.consumer.start()
    
    async def close(self):
        await self.producer.stop()
        await self.consumer.stop()

    async def stop_consuming(self):
        self.consumer.unsubscribe()
