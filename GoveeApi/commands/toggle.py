from constants import Constants
import json


def turn_on(MAC, MODEL, apiKey):
    payload = json.dumps({
        "device": MAC,
        "model": MODEL,
        "cmd": {
            "name": "turn",
            "value": "on"
        }
    })

    headers = {
        'Govee-API-Key': apiKey,
        'Content-Type': 'application/json'
    }

    Constants.Requests.call(payload, headers, "PUT",
                            Constants.Endpoints.DEVICE_CONTROL)


def turn_off(MAC, MODEL, apiKey):
    payload = json.dumps({
        "device": MAC,
        "model": MODEL,
        "cmd": {
            "name": "turn",
            "value": "off"
        }
    })

    headers = {
        'Govee-API-Key': apiKey,
        'Content-Type': 'application/json'
    }

    Constants.Requests.call(payload, headers, "PUT",
                            Constants.Endpoints.DEVICE_CONTROL)
