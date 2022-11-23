import json

import httpx


def equipamento():
    link=f"https://apiequipamentos.herokuapp.com/equipamento"
    request = httpx.get(link)
    todos = json.loads(request.text)
    return todos