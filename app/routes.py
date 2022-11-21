from flask import jsonify, render_template, flash

from app import app
from app.forms import EscolhaCidade,EscolhaCoordenadas
from app.process.openWearther import busca
from app.process.tempo import previsao


## def index vai carregar uma pagina html
@app.route('/')
@app.route('/index') 
def index():                
    return render_template('index.html')
## escolha vai recebe o nome da cidade  e vai retorna as informaçoes 
@app.route('/escolha', methods=['GET','POST'])
def escolha():
    form = EscolhaCidade() #pega as informaçoes do arquivo forms.py e retorna a cidade escolhida
    if form.validate_on_submit():#verifica se tem informaçoes no formulario
        cidade = form.cidade.data #pega a string do nome da cidade que veio do formulario
        previsao_infos = previsao(cidade) # passa o nome da cidade pro tempo.py e retorna as informaçoes do json 
        return render_template('previsao.html', previsao_infos=previsao_infos) # vai renderizar as informaçoes do html com o json 
    return render_template('escolha.html', form=form) #caso o form nao seja valido permanece na pagina escolha 

@app.route('/externa', methods=['GET','POST'])
def externa():
    form = EscolhaCoordenadas() #pega as informaçoes do arquivo forms.py e retorna a cidade escolhida
    if form.validate_on_submit():#verifica se tem informaçoes no formulario
        latitude = form.latitude.data
        longitude = form.longitude.data
        coordenadas =  busca(latitude,longitude)
      
        return render_template('api_externa.html',coordenadas=coordenadas) 
    return render_template('coordenadas.html', form=form) #caso o form nao seja valido permanece na pa


# @app.route('/previsao')
# def previsao():
#     cidade = 'lages'
#     return render_template('previsao.html', cidade=cidade)

# @app.route('/tempo/<cidade>', methods = ['GET'])
# def tempo(cidade):                
#     resultado = previsao(cidade)
#     if resultado == None:
#         return 'Cidade incorreta'
#     return jsonify({
#         'cidade': resultado['cidade'],
#         'clima': resultado['clima'],
#         'temperatura' : resultado['temperatura'],
#         'umidade' : resultado['umidade']
#         })

# @app.route('/nomes')
# def nomes():              
#     dados = busca()
#     filtrar_nome = ajusta_dados(dados)

#     return jsonify({
#         'resultado': filtrar_nome
#     })

# @app.route('/externa', methods=['GET','POST'])
# def externa(): #vai carregar os dados da api_externa 
#     dados=busca() #vai chamar no openWearther.py que vai consumir os dados 
#     return render_template('api_externa.html',dados= dados ) #renderizar a pagina 
   