from flask import jsonify, render_template, flash

from app import app
from app.forms import EscolhaCidade
from app.process.ibge import ajusta_dados, busca
from app.process.tempo import previsao


@app.route('/')
@app.route('/index')
def index():                
    return render_template('index.html')

@app.route('/escolha', methods=['GET','POST'])
def escolha():
    form = EscolhaCidade()
    if form.validate_on_submit():
        flash(f'{form.cidade.data}')
        cidade = form.cidade.data
        return render_template('previsao.html', cidade=cidade)
    return render_template('escolha.html', form=form)

@app.route('/previsao')
def previsao():
    cidade = 'lages'
    return render_template('previsao.html', cidade=cidade)

@app.route('/tempo/<cidade>', methods = ['GET'])
def tempo(cidade):                
    resultado = previsao(cidade)
    if resultado == None:
        return 'Cidade incorreta'
    return jsonify({
        'cidade': resultado['cidade'],
        'clima': resultado['clima'],
        'temperatura' : resultado['temperatura'],
        'umidade' : resultado['umidade']
        })

@app.route('/nomes')
def nomes():              
    dados = busca()
    filtrar_nome = ajusta_dados(dados)

    return jsonify({
        'resultado': filtrar_nome
    })

@app.route('/externa', methods=['GET','POST'])
def externa():
    return render_template('externa.html') 