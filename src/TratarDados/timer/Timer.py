import requests
import json
from threading import Thread
import time


class Timer(Thread):
    vezes = 1

    def __init__(self):
        Thread.__init__(self)
        self._user = 'user-public-notificacoes'
        self._password = 'Za4qNXdyQNSa9YaA'
        self._url = 'https://elasticsearch-saps.saude.gov.br/desc-notificacoes-esusve-*/_search?size=6000'
        self._dados = self.get_dados_service()

    def get_dados_service(self):

        request = requests.get(self._url, auth=(self._user, self._password))
        self._dados = json.loads(request.text)
        '''
        for x in range(len(self._dados['hits']['hits'])):
            print(self._dados['hits']['hits'][x]['_source']['resultadoTeste'])
        print('atualizou', self.vezes)
        '''

        self.vezes = self.vezes+1
        return self._dados

    def run(self):
        while(True):
            self._dados = self.get_dados_service()
            time.sleep(5)

    def get_dados(self):
        return self._dados


'''
t = Timer()

t.get_dados_service()
'''
