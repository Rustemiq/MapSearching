import requests
from io import BytesIO
from PIL import Image

map_api_server = "https://static-maps.yandex.ru/v1"


def show_map(pt):
    apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"

    map_params = {
        "apikey": apikey,
        "pt": pt
    }
    response = requests.get(map_api_server, params=map_params)
    im = BytesIO(response.content)
    opened_image = Image.open(im)
    opened_image.show()