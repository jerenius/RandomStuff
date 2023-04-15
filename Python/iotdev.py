
connstr = "HostName=SnakemanHUB.azure-devices.net;DeviceId=iohomedev;SharedAccessKey=7A3+4VHJJMYbfGMQN8fnCVxHD1F/x9aDwm/uZ9y/n6A="

import asyncio
import os
from azure.iot.device.aio import IoTHubDeviceClient


async def main():
    # Fetch the connection string from an enviornment variable
    conn_str =  connstr

    # Create instance of the device client using the connection string
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Send a single message
    print("Sending message...")
    await device_client.send_message("This is a message that is being sent")
    print("Message successfully sent!")

    # finally, disconnect
    await device_client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
