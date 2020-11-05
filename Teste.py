import requests
import json

# cep_input= input('Digite o CEP ')

request = requests.get('https://elasticsearch-saps.saude.gov.br/desc-notificacoes-esusve-rn/_search?q=estado=RIO GRANDE DO NORTE',
                       auth=('user-public-notificacoes', 'Za4qNXdyQNSa9YaA'))
data = json.loads(request.text)

tamanho = len(data['hits']['hits'])
for x in range(tamanho):
    print(data['hits']['hits'][x]['_source']['municipio'])

# print("indice ", data['municipio'])
