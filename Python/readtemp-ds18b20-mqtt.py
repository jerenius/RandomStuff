#!/usr/bin/python3

import os
import glob
import time
import json
import random
from paho.mqtt import client as mqtt_client

# setings for mqtt
broker = '10.0.4.11'
port = 1883
topic = "home/parveke/sensor/1"
client_id = 'parveke'
devicename = os.environ['mqttusername']
connstr = os.environ['mqttpassword'
# settings for 1-wire (ds18b20)
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
   f = open(device_file, 'r')
   lines = f.readlines()
   f.close()
   return lines

def read_temp():
   lines = read_temp_raw()
   while lines[0].strip()[-3:] != 'YES':
      time.sleep(0.2)
      lines = read_temp_raw()
   equals_pos = lines[1].find('t=')
   if equals_pos != -1:
      temp_string = lines[1][equals_pos+2:]
      temp_c = float(temp_string) / 1000.0
      temp_c = "{:.2f}".format(temp_c)
      json_data = json.dumps({"temperature_C": temp_c })
      return json_data

      def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    while True:
        msg = read_temp()
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        time.sleep(300)


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()