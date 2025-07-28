from aiokafka import AIOKafkaProducer
import asyncio

async def send_one():
    producer = AIOKafkaProducer(bootstrap_servers='kafka:29092')

    await producer.start()
    try:
        await producer.send_and_wait("test_topic", b"Super-puper message")
    finally:

        await producer.stop()

asyncio.run(send_one())