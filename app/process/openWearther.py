import json

import httpx


def busca(cep):
    link=f"https://viacep.com.br/ws/cep={cep}/json"
    request = httpx.get(link)
    todos = json.loads(request.text)
    return todos

def ajusta_dados(dados):
    nomes = []
    for pessoa in dados:
        nomes.append(pessoa['nome'])
    return nomes

