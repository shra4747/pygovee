from constants import Constants
import requests
import sys
import json
from commands import toggle, brightness, color


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
        toggle.turn_on(mac, model, self.apiKey)

    def device_off(self, mac, model):
        toggle.turn_off(mac, model, self.apiKey)

    def change_device_brightness(self, mac, model, brightness_level: int):
        brightness.change_brightness(mac, model, self.apiKey, brightness_level)

    def change_device_color(self, mac, model, r: int, g: int, b: int):
        color.change_color(mac, model, self.apiKey, r, g, b)


client = GoveeClient(apiKey="095cfe5a-3e8d-430d-95a3-c23336a822cc")
client.device_on("AB:B7:A4:C1:38:BE:1C:6D", "H6159")
