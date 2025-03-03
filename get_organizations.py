import requests
import sys

api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
search_api_server = "https://search-maps.yandex.ru/v1/"


def get_organizations(address_ll, qty):
    search_params = {
        "apikey": api_key,
        "text": "аптека",
        "lang": "ru_RU",
        "ll": address_ll,
        "type": "biz"
    }

    response = requests.get(search_api_server, params=search_params)

    if not response:
        print('Ошибка выполнения запроса')
        print(response.status_code)
        sys.exit()

    json_response = response.json()

    organization = json_response["features"][:qty]
    return organization