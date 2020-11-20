
from timer.Timer import Timer


class TratarDados:

    def __init__(self):
        self._dados = dict
        self._paciente = {'id': '', 'sexo': '',
                          'sintomas': '', 'profissional_saude': '', 'endereco': ''}
        self._paciente = {'municipio': '', 'estado': ''}

    def ObterDadosPaciente(self, dados):
        tamanho = len(dados)
        # print(dados)
        for x in range(tamanho):
            self._paciente['id'] = dados['hits']['hits'][x]['_source']['source_id']
            self._paciente['sexo'] = dados['hits']['hits'][x]['_source']['sexo']
            self._paciente['idade'] = dados['hits']['hits'][x]['_source']['idade']
            self._paciente['endereco'] =

            print(self._paciente['id'])
            print(self._paciente['sexo'])

    def ObterDadosEndereco(self, dados):
        self._paciente['idade'] = dados['hits']['hits'][x]['_source']['idade']


t = Timer()
t.start()
dados = t.dados
tr = TratarDados()
tr.ObterDadosPaciente(dados)
