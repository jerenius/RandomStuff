// simple mqtt test
// requires npm install mqtt


const mqtt = require('mqtt')
const client = mqtt.connect('mqtt://10.0.4.105')

var connected = false
var sensor =''

client.on('connect', () => {
  client.subscribe('#')
})

client.on('message', (topic, message) => {  switch (topic) {
    case 'temp/1':
      sensor=topic.replace('/','')
      return handleSensorValue(message,topic)
    case 'temp/2':
       sensor=topic.replace('/','')
      return handleSensorValue(message,topic)
    case 'temp/3':
       sensor=topic.replace('/','')
       return handleSensorValue(message,topic)
  }
  console.log('No handler for topic %s', topic)
})

function handleSensorValue (message,topic) {
  console.log('%s update to %s (%s)',sensor, message, topic)
}

