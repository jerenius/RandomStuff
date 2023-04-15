#!/usr/bin/python3

import paho.mqtt.client as mqtt #import the client1
import Adafruit_DHT as dht
import os
import asyncio
import time

devicename = 'dhttest'
broker_address='10.0.4.105'
client = mqtt.Client(devicename)
h,t = dht.read_retry(dht.DHT22, 4)
h='{0:0.2f}'.format(h)
t='{0:0.2f}'.format(t)
client.connect(broker_address)
client.publish('temp/4',t)
client.publish('hum/4',h)

