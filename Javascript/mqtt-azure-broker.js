const azClient = require('azure-iot-device').Client;
const Message = require('azure-iot-device').Message;
const Protocol = require('azure-iot-device-mqtt').Mqtt;
const mqtt = require('mqtt')
const azconnectionString = process.env.connectionstring
const mqttclient = mqtt.connect("mqtt://" + process.env.mqttbroker)

var connected = false
var sensor

// connect to azure IoT Hub
var azclientFromConnectionString = require('azure-iot-device-mqtt').clientFromConnectionString;
var azclient = azclientFromConnectionString(azconnectionString);
var azmessage = require('azure-iot-device').Message;

// connect mqtt broker and subscribe
mqttclient.on('connect', () => {
  mqttclient.subscribe('#')
})

// receive message from broker
mqttclient.on('message', (topic, message) => {
      sensor=topic.replace('/','')
      message = message.toString()
      return handleSensorValue(message,topic)
})

function handleSensorValue (message,topic) {
  var content= JSON.stringify({
    sensor: sensor,
    value: message

  })
  var azmsg = new azmessage(content);
  azclient.sendEvent(azmsg);

//  console.log(content)


}


