import random
from datetime import date
def previsao(cidade):
    cidades = open("app\process\cidades.txt", 'r').readlines()
    data= date.today()
    if (cidade+'\n') in cidades:
        resultado = [{
            'cidade': cidade,
            'data':((data.day),(data.month)),
            'clima': random.choice(climas),
            'temperatura' : random.randrange(1,40),
            'umidade': random.randrange(1,100)
        },{
            'cidade': cidade,
            'data':((data.day+1),(data.month)),
            'clima': random.choice(climas),
            'temperatura' : random.randrange(1,40),
            'umidade': random.randrange(1,100)
        },{
            'cidade': cidade,
            'data':((data.day+2),(data.month)),
            'clima': random.choice(climas),
            'temperatura' : random.randrange(1,40),
            'umidade': random.randrange(1,100)
        },{
            'cidade': cidade,
            'data':((data.day+3),(data.month)),
            'clima': random.choice(climas),
            'temperatura' : random.randrange(1,40),
            'umidade': random.randrange(1,100)
        },{
            'cidade': cidade,
            'data':((data.day+4),(data.month)),
            'clima': random.choice(climas),
            'temperatura' : random.randrange(1,40),
            'umidade': random.randrange(1,100)
        }]
        return resultado
    return None

climas = [
    'nublado',
    'céu limpo',
    'chuva',
    'tempestade',
]
