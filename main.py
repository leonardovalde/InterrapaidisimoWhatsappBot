import requests

import time

import properties


guide_number = properties.guide
phone_number = properties.phoneNumber
api_key = properties.apiKey

package_request =  response = requests.get(f'https://www3.interrapidisimo.com/ApiServInter/api/Mensajeria/ObtenerRastreoGuias?guias={guide_number}')

json_data = (package_request.json()[0])["TrazaGuia"]
guide_status = json_data["DescripcionEstadoGuia"]
whatsapp_api_url_request = f'https://api.callmebot.com/whatsapp.php?phone={phone_number}&text="{guide_status}"&apikey={api_key}'
requests.get(whatsapp_api_url_request)

while True:
    ackage_request =  response = requests.get(f'https://www3.interrapidisimo.com/ApiServInter/api/Mensajeria/ObtenerRastreoGuias?guias={guide_number}')
    json_data = (package_request.json()[0])["TrazaGuia"]
    guide_status_aux = json_data["DescripcionEstadoGuia"]
    if guide_status != guide_status_aux:
        guide_status = guide_status_aux
        requests.get(whatsapp_api_url_request)
    time.sleep(600)