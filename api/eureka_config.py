# eureka_config.py

import asyncio
import socket
from py_eureka_client.eureka_client import EurekaClient

def get_ip_address():
    """Get the IP address of the local machine."""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

async def start_eureka_client():
    # Initialize Eureka client

    # Get the local machine's IP address
    ip_address = get_ip_address()
    print(ip_address)
    eureka_client = EurekaClient(
        eureka_server="https://ntic-discovery-server2.onrender.com/eureka/",
        app_name="price_prediction",
        instance_port=8000,  # The port your Django app is running on
        instance_ip=ip_address,  # The IP address your Django app is running on
        renewal_interval_in_secs=30,  # Heartbeat interval
        duration_in_secs=90  # Expiry duration
    )

    # Start the Eureka client
    await eureka_client.start()

def run_eureka_client():
    asyncio.run(start_eureka_client())
