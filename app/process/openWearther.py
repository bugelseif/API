import json

import httpx


def busca(latitude,longitude):
    latitude=latitude
    longitude=longitude
    link=f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}8&lon={longitude}&appid=1810eb105d64626022f2340b13d6f82d"
    request = httpx.get(link)
    todos = json.loads(request.text)
    return todos

def ajusta_dados(dados):
    nomes = []
    for pessoa in dados:
        nomes.append(pessoa['nome'])
    return nomes

