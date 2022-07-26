import requests
import sys
import json


class Constants:
    class Endpoints:
        DEVICE_LIST = 'https://developer-api.govee.com/v1/devices'
        DEVICE_CONTROL = 'https://developer-api.govee.com/v1/devices/control'

    class Requests:
        def call(payload, headers, method, url):
            response = requests.request(
                method, url, headers=headers, data=payload)

            if response.status_code != 200:
                sys.exit(f'ERROR: HTTP Status Code: {response.status_code}')

            return response


class GoveeClient:
    def __init__(self, apiKey):
        self.apiKey = apiKey

    def login(self):
        response = Constants.Requests.call(
            {}, {'Govee-API-Key': self.apiKey}, "GET", Constants.Endpoints.DEVICE_LIST)

        return (True, response)

    def get_device_list(self):
        response = self.login()
        devices = response[1].json()['data']['devices']
        for device in devices:
            print(
                f"\033[1m{device['deviceName']}:\033[0m \033[1mMAC_ADDRESS:\033[0m {device['device']}, \033[1mMODEL:\033[0m: {device['model']}")

    def device_on(self, mac, model):
        payload = json.dumps({
            "device": mac,
            "model": model,
            "cmd": {
                "name": "turn",
                "value": "on"
            }
        })

        headers = {
            'Govee-API-Key': self.apiKey,
            'Content-Type': 'application/json'
        }

        Constants.Requests.call(payload, headers, "PUT",
                                Constants.Endpoints.DEVICE_CONTROL)

    def device_off(self, mac, model):
        payload = json.dumps({
            "device": mac,
            "model": model,
            "cmd": {
                "name": "turn",
                "value": "off"
            }
        })

        headers = {
            'Govee-API-Key': self.apiKey,
            'Content-Type': 'application/json'
        }

        Constants.Requests.call(payload, headers, "PUT",
                                Constants.Endpoints.DEVICE_CONTROL)

    def change_device_brightness(self, mac, model, brightness_level: int):
        payload = json.dumps({
            "device": mac,
            "model": model,
            "cmd": {
                "name": "brightness",
                "value": brightness_level
            }
        })

        headers = {
            'Govee-API-Key': self.apiKey,
            'Content-Type': 'application/json'
        }

        Constants.Requests.call(payload, headers, "PUT",
                                Constants.Endpoints.DEVICE_CONTROL)

    def change_device_color(self, mac, model, r: int, g: int, b: int):
        payload = json.dumps({
            "device": mac,
            "model": model,
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
            'Govee-API-Key': self.apiKey,
            'Content-Type': 'application/json'
        }

        Constants.Requests.call(payload, headers, "PUT",
                                Constants.Endpoints.DEVICE_CONTROL)