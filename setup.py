from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.2'
DESCRIPTION = 'Python Wrapper for Govee API'
LONG_DESCRIPTION = '''
# pygovee
A Python wrapper for the HTTP Govee Developer API to control Govee WiFi supported devices.
*Developed by Shravan Prasanth (c) 2022.*
![python](https://img.shields.io/badge/python-%3E3-9cf?style=for-the-badge&logo=python) ![os](https://img.shields.io/badge/os-ALL-orange?style=for-the-badge&logo=all)

## Installation
```bash
pip3 install pygovee==1.0.2
```

or

```bash
pip install pygovee==1.0.2
```

## Usage

****Retreive API Key from Govee Home App (Profile → About Us → Apply for API Key)**

***10 requests per minute per device

```python
from pygovee import Govee

client = Govee.GoveeClient(apiKey="<your api key>")
client.login()
```

### Get Device List

**Mock MAC Address and Model, THIS DATA WON'T WORK!
```python
client.get_device_list()
# Kitchen Lights: MAC_ADDRESS: 3E-C7-8A-95-A5-40, MODEL:: H6159
# Bedroom Lights: MAC_ADDRESS: 23-14-96-F0-0D-58, MODEL:: H6159
```

**Replace <DEVICE_MAC_ADDRESS> and <DEVICE_MODEL> with your device information when running the command above.**
### Turn Devices On and Off
```python
client.device_on("<DEVICE_MAC_ADDRESS>", "<DEVICE_MODEL>")
client.device_off("<DEVICE_MAC_ADDRESS>", "<DEVICE_MODEL>")
```

### Change Device Brightness
brightness_level should be an `int`!
```python
client.change_device_brightness(
	"<DEVICE_MAC_ADDRESS>", "<DEVICE_MODEL>", brightness_level
)
```

### Change Device Color using R,G,B Values
r_value, g_value, b_value should all be an `int`!
```python
client.change_device_color(
	"<DEVICE_MAC_ADDRESS>", "<DEVICE_MODEL>", r_value, g_value, b_value
)
```
'''

# Setting up
setup(
    name="pygovee",
    version=VERSION,
    author="Shravan Prasanth",
    author_email="<shravanapps44@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    project_urls={
        'GitHub': 'https://github.com/shra4747/python-govee'
    },
    install_requires=['requests'],
    keywords=['python', 'govee', 'api',
              'govee home', 'govee developer', 'lights'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
