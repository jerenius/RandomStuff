#!/usr/bin/python3

#import Adafruit_BMP.BMP085 as BMP085
import paho.mqtt.client as mqtt #import the client1
import os
import asyncio
import time
from numpy.random import seed
from numpy.random import randint
from azure.iot.device.aio import IoTHubDeviceClient

devicename = os.environ['devicename']
connstr = os.environ['connectionstring']

while True:
  #sensor = BMP085.BMP085()
  broker_address='10.0.4.105'
  client = mqtt.Client(devicename) 
  #temperature = '{0:0.2f}'.format(sensor.read_temperature())
  temperature = randint(20,30)
  #temperature = "{temp: " +temperature + ", device: "+ devicename +"}"
  client.connect(broker_address) 
  client.publish("temp/2",temperature) 
  time.sleep(50)

#async def main():
#  device_client = IoTHubDeviceClient.create_from_connection_string(connstr)
#  await device_client.send_message(temperature)
#  await device_client.disconnect()
#if __name__ == "__main__":
#    asyncio.run(main())

