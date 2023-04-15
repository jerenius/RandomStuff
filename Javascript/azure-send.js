const Client = require('azure-iot-device').Client;
const Message = require('azure-iot-device').Message;
const Protocol = require('azure-iot-device-mqtt').Mqtt;
const mqtt = require('mqtt')
const mqttclient = mqtt.connect('mqtt://10.0.4.105')
const connectionstring = process.env.connectionstring

var connected = false
var sensor

mqttclient.on('connect', () => {
  mqttclient.subscribe('#')
})

mqttclient.on('message', (topic, message) => {
      sensor=topic.replace('/','')
      message = message.toString()
      return handleSensorValue(message,topic)
})




var connectionString =  process.env.connectionstring


sendMessage = function(){

            var content = JSON.stringify({
            messageId: messageId++,
            deviceId: 'RaspPiTemp',
            temperature: '23.50',
            humidity: '40',
            time:new Date()
            });

            var message = new Message(content);
            console.log('Sending message: ' + content);
            azclient.sendEvent(message, (err) => {
            if (err) {
                console.error('Failed to send message to Azure IoT Hub');
            } else {
                console.log('Message sent to Azure IoT Hub');
            }
            setTimeout(sendMessage, 1000);
            });
};

receiveMessageCallback = function(msg) {
    var message = msg.getData().toString('utf-8');
    azclient.complete(msg, () => {
      console.log('Receive message: ' + message);
    });
  }


var azclient = Client.fromConnectionString(connectionString, Protocol);
messageId =0;
azclient.open((err) => {
    if (err) {
      console.error('[IoT hub Client] Connect error: ' + err.message);
      return;
    }
    azclient.on('disconnect',function(){
        azclient.removeAllListeners();
        console.log('client disconnected');
    });
    azclient.on('message', receiveMessageCallback);
    sendMessage();
});
