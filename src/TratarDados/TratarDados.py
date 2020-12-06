#from timer.Timer import Timer


class TratarDados:

    def __init__(self):
        self._dados = dict
        self._paciente = {}
        self._endereco = {'municipio': '', 'estado': ''}
        self._teste = {'data_teste': '',
                       'data_notificacao': '', 'resultado': '',
                       'data_encerramento': '', 'sintomas': '',
                       'data_inicio_sintomas': '', 'classificacao': '', 'estado_teste': '',
                       'condicoes': '', 'evolucao_caso': ''}

    def ObterDadosPaciente(self, dados):
        tamanho = len(dados['hits']['hits'])
        print(tamanho)
        # print(dados)
        for x in range(tamanho):
            paciente = {
                x: {'CBO': dados['hits']['hits'][x]['_source']['cbo'],
                    'sexo': dados['hits']['hits'][x]['_source']['sexo'],
                    'proficional_saude': dados['hits']['hits'][x]['_source']['profissionalSaude'],
                    # 'profissional_de_seguranca ': dados['hits']['hits'][x][''],
                    'idade': dados['hits']['hits'][x]['_source']['idade'],
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
           # self._endereco['pais'] = dados['hits']['hits'][x]['_source']['']

        return self._endereco

    def ObterDadosTestes(self, dados):
        for x in range(len(dados)):
            self._teste['data_teste'] = dados['hits']['hits'][x]['_source']['dataTeste']
            self._teste['data_encerramento'] = dados['hits']['hits'][x]['_source']['dataEncerramento']
            self._teste['data_notificacao'] = dados['hits']['hits'][x]['_source']['dataNotificacao']
            self._teste['resultado'] = dados['hits']['hits'][x]['_source']['resultadoTeste']
            self._teste['sintomas'] = dados['hits']['hits'][x]['_source']['sintomas']
            self._teste['data_inicio_sintomas'] = dados['hits']['hits'][x]['_source']['dataInicioSintomas']
            self._teste['classificacao'] = dados['hits']['hits'][x]['_source']['classificacaoFinal']
            self._teste['estado_teste'] = dados['hits']['hits'][x]['_source']['estadoTeste']
            self._teste['condicoes'] = dados['hits']['hits'][x]['_source']['condicoes']
            #self._teste['descr_sintomas_outros']= dados['hits']['hits'][x]['_source']['']
            self._teste['evolucao_caso'] = dados['hits']['hits'][x]['_source']['evolucaoCaso']
            #self._teste['data_coleta'] = dados['hits']['hits'][x]['_source']['']

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
