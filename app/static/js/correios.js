function buscaDadosCEP(){
    var $cep = document.getElementById("cep").value.replace(/\D/g, '');
    var url = 'https://viacep.com.br/ws/' + $cep + '/json/';
    var request = new XMLHttpRequest();

    request.open('GET',url);
    request.onerror = function(e){
        document.getElementById('return').innerHTML = 'A API ViaCep esta fora ou CEP é invalido!'
    }
    request.onload = () => {
        var response = JSON.parse(request.responseText);
        
        if(response.erro === true){
            document.getElementById('return').innerHTML = 'CEP NÃO ENCONTRADO';
        }
        else
        {
            document.getElementById('return').innerHTML =
            'CEP: ' + response.cep + '<br>' +
            'Logradouro: ' + response.logradouro + '<br>' +
            'Bairro: ' + response.bairro +'<br>' +
            'Cidade: ' + response.localidade + '<br>' +
            'Estado: '+ response.uf + '<br>' +
            'Código IBGE: ' + response.ibge + '<br>' +
            'DDD: ' + response.ddd;
        }
    }
    request.send();
}
/* dificuldades para implementar essa consulta:
    rodar o projeto localhost e fazer consultas a uma api externa pelo navegador, retornava 'Acess-Control-Allow-Origin'
    que trata-se de um cabeçalho CORS "mecanismo que os navegadores têm para 
    permitir que um site em execução no ponto de origem A solicite recursos no ponto de origem B."
    Foi resolvido criando um arquivo headers.config.js que contêm os valores necessários para poder realizar a requisição externa
*/
