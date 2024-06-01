# eureka_config.py

import asyncio
from py_eureka_client.eureka_client import EurekaClient

async def start_eureka_client():
    # Initialize Eureka client
    eureka_client = EurekaClient(
        eureka_server="https://ntic-discovery-server2.onrender.com/eureka/",
        app_name="price_prediction",
        instance_port=8000,  # The port your Django app is running on
        instance_ip="127.0.0.1",  # The IP address your Django app is running on
        instance_id="price_prediction",
        renewal_interval_in_secs=30,  # Heartbeat interval
        duration_in_secs=90  # Expiry duration
    )

    # Start the Eureka client
    await eureka_client.start()

def run_eureka_client():
    asyncio.run(start_eureka_client())
