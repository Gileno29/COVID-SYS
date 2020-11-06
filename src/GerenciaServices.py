import requests
import json


# cep_input= input('Digite o CEP ')


class GerenciaServices:
    # _url = ''
    def __init__(self):
        self._user = 'user-public-notificacoes'
        self._password = 'Za4qNXdyQNSa9YaA'
        self._url = 'https://elasticsearch-saps.saude.gov.br/desc-notificacoes-esusve-*/_search?size=100'

    def get_dados_service(self):
        request = requests.get(self._url, auth=(self._user, self._password))
        self.dados = json.loads(request.text)

        return self.dados

    def get_info(self, dados):
        #print('entrei aqui')
        # print(type(dados))
        self.tamanho = len(dados)
        self.nome = []
        for x in range(self.tamanho):
            # print("==================================================================================================")
            # print("===========================SEÇÃO {}".format(x),
            #   "de dados=======================================")
            # print("==================================================================================================")
            # print(dados['hits']['hits'][x]['_source']['source_id'])
            self.nome.append(dados['hits']['hits'][x]['_source'])

        return self.nome
        # pass

        # print("indice ", data['municipio'])
