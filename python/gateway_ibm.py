import wiotp.sdk.gateway
import errno
import json
import os
import utils

class IbmGateway:

    myConfig = None
    gateway = None

    def __init__(self, config="ibm_conf.json"):
        self.loadConfig(config)
        self.initIbmGateway()

    def initIbmGateway(self):
        self.gateway = wiotp.sdk.gateway.GatewayClient(config=self.myConfig)

    def connect(self):
        self.gateway.connect()

    def disconnect(self):
        self.gateway.disconnect()

    def loadConfig(self, config):
        if config != "ibm_conf.json":
            filePath = config
        else:
            filePath = os.path.dirname(os.path.abspath(__file__)) + "/" + config
        if os.path.exists(filePath):
            config_file =  open(filePath, "r")
            self.myConfig = json.loads(config_file.read())
            config_file.close()
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filePath)

    def publisEvent(self, payload, callback=None):
        devId = utils.getDeviceId(payload)
        devType = utils.getDeviceType(payload)
        devData = utils.getDeviceData(payload)
        eventType = utils.getEventType(payload)
        self.gateway.publishDeviceEvent(typeId=devType, deviceId=devId, eventId=eventType, msgFormat="json", data=devData, qos=0, onPublish=callback)


if __name__ == "gateway_ibm":
    ibmGateway = IbmGateway()