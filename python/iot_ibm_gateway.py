import utils
import gateway_ibm as ibm
import mqtt_sub as mqtt

from signal import signal, SIGINT
from sys import exit

def mqtt_disconnect(client, userdata, rc):
    print("Mqtt disconnected succesfully")

def kill_handler(signal_received, frame):
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    mqtt.mqttSub.disconnect(mqtt_disconnect)
    ibm.ibmGateway.disconnect()
    exit(0)

def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    
    if  not utils.isJson(payload) and utils.emptyJson(payload):
        return 1

    ibm.ibmGateway.publisEvent(payload)

def main():
    ibm.ibmGateway.connect()
    mqtt.mqttSub.connect()
    mqtt.mqttSub.messageReceived(on_message)
    while True:
        mqtt.mqttSub.loopStart()

if __name__ == "__main__":
    signal(SIGINT, kill_handler)
    main()