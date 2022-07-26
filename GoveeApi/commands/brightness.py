from constants import Constants
import json


def change_brightness(MAC, MODEL, apiKey, brightness_level: int):
    payload = json.dumps({
        "device": MAC,
        "model": MODEL,
        "cmd": {
            "name": "brightness",
            "value": brightness_level
        }
    })

    headers = {
        'Govee-API-Key': apiKey,
        'Content-Type': 'application/json'
    }

    Constants.Requests.call(payload, headers, "PUT",
                            Constants.Endpoints.DEVICE_CONTROL)
