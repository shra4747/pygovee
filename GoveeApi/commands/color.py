from constants import Constants
import json


def change_color(MAC, MODEL, apiKey, r: int, g: int, b: int):
    payload = json.dumps({
        "device": MAC,
        "model": MODEL,
        "cmd": {
            "name": "color",
            "value": {
                "r": r,
                "g": g,
                "b": b
            }
        }
    })

    headers = {
        'Govee-API-Key': apiKey,
        'Content-Type': 'application/json'
    }

    Constants.Requests.call(payload, headers, "PUT",
                            Constants.Endpoints.DEVICE_CONTROL)
