import asyncio
from gmqtt import Client as MQTTClient
import logging

async def on_message(client, topic, payload, qos, properties):
    logging.info(f"Received message on topic '{topic}': {payload.decode()}")

async def connect_to_broker():
    client = MQTTClient("client-id")
    client.on_message = on_message

    await client.connect("localhost")

    async def subscribe():
        await client.subscribe("test/topic")

    await asyncio.wait([subscribe()])

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(connect_to_broker())
