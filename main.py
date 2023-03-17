import requests

import time

import properties


guide_number = properties.guide
phone_number = properties.phoneNumber
api_key = properties.apiKey

status =  response = requests.post(url, json=data)
    status_Code = response.status_code

whatsapp_api_url_request = f'https://api.callmebot.com/whatsapp.php?phone={phone_number}&text="+status+"&apikey={api_key}'

print(whatsapp_api_url_request)