# Descricao

O nosso api  é sobre a previsao do tempo onde podemos escolher uma cidade e ele retorna a previsao dessa cidade a atual e ate o proximos 5 dias.

## objetivos 
Construit a nossa api.E cosnumir  uma externa e de um colega

## fluxo 
 na pagina inicial (index) tem uma barra de menus com algumas opçoes, A nossa api a api externa e api de outros 

### meteorologica api local
Na api local tem um menu com a lista de cidades 
eu posso selecionar uma cidade pra retorna a previsao do tempo, onde vai nos mostrar algumas carateristicas do clima como nublado,tempestade,chuva e ceu limpo dentro de cards e a temperatura conrrespondnete 

* Como funciona 
 As opçoes estao na rota /escolha (escolha.html) 
 nela carrega um formulario (forms.py) onde nele esta lendo um arquivo de texto com os nomes das cidades e esta colocando eles dentro de uma lista de escolha e esta lista e colocada em uma selectField 
 e o botao de submit que envia a cidade escolha para o processamento.
 * Essa rota faz a validacao do nome da cidade que foi recebida, ele guarda na variavel cidade e envia para o processamento  e tem o retorno das informaçoes, quando envia o processamento esta enviando para o (tempo.py)
a funcao de previsao vai retorna um json com as informaçoes a cidade escolhida data de hj e mais cinco dias  clima temperatura e umidade sao dados aleatorios ele pega essas informaçoes e retorna pra rota(routes.py) todas essas informaçoes estao na variavel previsao-infos essas informaçoes serao carregas em uma nova pagina que e a (previsao.html) 
* previsao.html --> vai receber as informaçoes do json e vai receber de todos os dias e vai entrar em uma laço de repeticao onde vai carregar  cada dia em card diferente 

