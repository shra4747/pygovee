import requests
import sys


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
