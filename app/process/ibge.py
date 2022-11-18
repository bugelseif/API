import json

import httpx


def busca():
    request = httpx.get("https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=1810eb105d64626022f2340b13d6f82d")
    todos = json.loads(request.text)
    return todos

def ajusta_dados(dados):
    nomes = []
    for pessoa in dados:
        nomes.append(pessoa['nome'])
    return nomes

