import paho.mqtt.client as mqtt
import errno
import json
import os

class MqttSub:

    brokerAddress = None
    brokerPort = None
    clientName = None
    subscriber = None
    topics = []
    subTopics = []

    def __init__(self, config="mqtt_conf.json"):
        self.loadConfig(config)
        self.initMqttSub()

    def initMqttSub(self):
        self.subscriber = mqtt.Client(self.clientName)

    def connect(self):
        self.subscriber.connect(host=self.brokerAddress,port=self.brokerPort)
        self.loadTopics(self.topics)

    def loadConfig(self, config):
        if config != "mqtt_conf.json":
            filePath = config
        else:
            filePath = os.path.dirname(os.path.abspath(__file__)) + "/" + config
        if os.path.exists(filePath):
            configFile =  open(filePath, "r")
            confData = json.loads(configFile.read())
            self.brokerAddress = confData['mqtt_sub']['broker_address']
            self.brokerPort = confData['mqtt_sub']['broker_port']
            self.clientName = confData['mqtt_sub']['client_name']
            self.topics = confData['topics']
            configFile.close()
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filePath)

    def loadTopics(self, topics):
        for i in range(len(topics)):
            self.subscribe(topics[i])

    def subscribe(self, topic):
        if topic:
            self.subscriber.subscribe(topic)
            self.subTopics.append(topic)

    def getTopics(self):
        for i in range(len(self.subTopics)):
            print(str(i+1) + " -- " + self.subTopics[i])

    def disconnect(self, callback=None):
        self.subscriber.on_disconnect = callback
        self.subscriber.disconnect()
        self.subscriber.on_disconnect = callback

    def messageReceived(self, callback=None):
        self.subscriber.on_message = callback

    def loopStart(self):
        self.subscriber.loop_start()

if __name__ == "mqtt_sub":
    mqttSub = MqttSub()
    # print("The value of __name__ is:", repr(__name__))
