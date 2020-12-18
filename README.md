# Simple-ibm-watson-gateway
This repository stores a simple IBM watson internet of things service gateway project for home usage

## How to
This gateway subscribes to your specified topics over Mqtt. All subscribed topics are forwarded to IBM Watson Internet of Things service.

To run this project you have to have a [IBM Watson](https://cloud.ibm.com/login) account. This account is used for data monitoring of your devices using [IBM IoT service](https://internetofthings.ibmcloud.com/). And install an MQTT Broker. This project was tested with [Mosquitto](https://mosquitto.org/) with Raspberry PI.

To configure MQTT client use **mqtt_conf.json** file.

To configure IBM Watson client use **ibm_conf.json** file. For full configuration example see this manual page [IBM gateway config](https://ibm-watson-iot.github.io/iot-python/gateway/config/)

To run this project you need at least **Python3.6** version and install these two dependencies:
* [Paho MQTT](https://pypi.org/project/paho-mqtt/#constructor-reinitialise)
* [IBM Watson](https://github.com/ibm-watson-iot/iot-python)

Or run these commands:
```
pip install wiotp-sdk
pip install paho-mqtt
```
If you have **Python2** and **Python3** installed, yuo can use **pip3** to install the necessary dependencies.

## Device configuration

Your device must publis information over MQTT to your specified topic. Also don't forget that the server needs to subscribe to your topic.

The device must sent [JSON](https://www.w3schools.com/whatis/whatis_json.asp) format messages. The format of the message:
```
{
   "device":{
      "deviceId":"<device_id>",
      "deviceType":"<device_type_id>",
      "eventType":"<event_type>"
   },
   "data":{
      "<your_specified_attribute>": "<attribute_data>"
   }
}
```

## To Do
* Add security functionality for the MQTT in the local network
* Add Access control functionality
