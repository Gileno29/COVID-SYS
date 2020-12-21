from flask import render_template
from flask import Flask
from flask import jsonify
from flask import request
from flask import redirect
from Filtro import Filtro
import requests
import json
import time

dados=''

# subsequent requests
i=0
response = requests.get('https://elasticsearch-saps.saude.gov.br/desc-notificacoes-esusve-*/_search?size=10000',auth=('user-public-notificacoes', 'Za4qNXdyQNSa9YaA'), params=post)
dados= json.loads(response.text)
print("Todos os registros na posicao",i,"\n", dados)
i=0
while(i<100000):
    post={
        'size':10000,
        'from':i+1000
    }
    response = requests.get('https://elasticsearch-saps.saude.gov.br/desc-notificacoes-esusve-*/_search?',auth=('user-public-notificacoes', 'Za4qNXdyQNSa9YaA'), params=post)
    dados= json.loads(response.text)
