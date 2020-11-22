
#from timer.Timer import Timer


class TratarDados:

    def __init__(self):
        self._dados = dict
        self._paciente = {}
        self._endereco = {'municipio': '', 'estado': ''}
        self._teste = {'data_teste': '',
                       'data_notificacao': '', 'resultado': ''}

    def ObterDadosPaciente(self, dados):
        tamanho = len(dados['hits']['hits'])
        print(tamanho)
        # print(dados)
        for x in range(tamanho):
            paciente = {
                x: {'id': dados['hits']['hits'][x]['_source']['source_id'],
                    'sexo': dados['hits']['hits'][x]['_source']['sexo'],
                    'idade': dados['hits']['hits'][x]['_source']['idade'],
                    'sintomas': dados['hits']['hits'][x]['_source']['sintomas'],
                    'teste': self.ObterDadosTestes(dados),
                    'endereco': self.ObterDadosEndereco(dados)}}
            '''print(self._paciente[x]['id'])
            print(self._paciente[x]['sexo'])
            print(self._paciente[x]['endereco'])'''
            # print(self._paciente)
            self._paciente.update(paciente)
        return self._paciente

    def ObterDadosEndereco(self, dados):
        for x in range(len(dados)):
            self._endereco['municipio'] = dados['hits']['hits'][x]['_source']['municipio']
            self._endereco['estado'] = dados['hits']['hits'][x]['_source']['estado']

        return self._endereco

    def ObterDadosTestes(self, dados):
        for x in range(len(dados)):
            self._teste['data_teste'] = dados['hits']['hits'][x]['_source']['dataTeste']
            self._teste['data_notificacao'] = dados['hits']['hits'][x]['_source']['dataNotificacao']
            self._teste['resultado'] = dados['hits']['hits'][x]['_source']['resultadoTeste']
        return self._teste


# teste de funcionamento da classe
'''
t = Timer()
t.start()
dados = t.get_dados()

print('#################### DADOS NA CLASSE TRATAR DADOS##############################')
# print(dados, '\n')
# print(len(dados['hits']['hits']))

# print(dados)
tr = TratarDados()
print(tr.ObterDadosPaciente(dados))
'''
