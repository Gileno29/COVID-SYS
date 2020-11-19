
from timer.Timer import Timer


class TratarDados:

    def __init__(self):
        self._dados = dict
        self._paciente = {'id': '', 'sexo': '',
                          'sintomas': '', 'profissional_saude': ''}

    def ObterDadosPaciente(self, dados):
        tamanho = len(dados)
        # print(dados)
        for x in range(tamanho):
            self._paciente['id'] = dados['hits']['hits'][x]['_source']['source_id']
            print(self._paciente['id'])


t = Timer()
t.start()
dados = t.dados
tr = TratarDados()
tr.ObterDadosPaciente(dados)
