import json

def getDeviceId(payload):
    if not payload:
        return None
    try:
        data = json.loads(payload)
        return data['device']['deviceId']
    except:
        return None

def getDeviceType(payload):
    if not payload:
        return None
    try:
        data = json.loads(payload)
        return data['device']['deviceType']
    except:
        return None

def getEventType(payload):
    if not payload:
        return None
    try:
        data = json.loads(payload)
        return data['device']['eventType']
    except:
        return None

def getDeviceData(payload):
    if not payload:
        return None
    try:
        data = json.loads(payload)
        return data['data']
    except:
        return None

def isJson(jsonOString):
    try:
        json.loads(jsonString)
        return 1
    except:
        return 0

def emptyJson(jsonString):
    try:
        jsonObject = json.loads(jsonString)
        if len(jsonObject) > 0:
            return 0
        else:
            return 1
    except:
        return 1
