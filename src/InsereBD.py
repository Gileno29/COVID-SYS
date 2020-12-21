import requests
import json
from threading import Thread
import time
from TratarDados.TratarDados import TratarDados
from TratarDados.timer import Timer
from persistencia.conexao import Conexao
from entities.Paciente import Paciente
from entities.Endereco import Endereco
from entities.Teste import Teste
from datetime import datetime
from TratarData import TratarData
import threading 
import random


class InsereBD(Thread):
    vezes = 1

    def __init__(self):
        Thread.__init__(self)
        self._user = 'user-public-notificacoes'
        self._password = 'Za4qNXdyQNSa9YaA'
        self._url = 'https://elasticsearch-saps.saude.gov.br/desc-notificacoes-esusve-pb/_search?size=10000'
        #self._dados = self.get_dados_service()
        self._con = Conexao.Conexao().conectar()
        self._i = 0
        self._count=0
        self._inserido=True

    def get_dados_service(self):
        
        post={
        'size':10000,
        'from':self._i
            }
        request = requests.get(self._url, auth=(self._user, self._password), params=post)
        dados = json.loads(request.text)
        self._i= self._i + 10000
        if(self._i==1000000):
            return print('Registros finalizados')
        self.persistir(dados)
       


        #self.vezes = self.vezes+1
        #return self._dados



    def get_dados(self):
        return self._dados

    def persistir(self, dados):
        dados = dados
        
        self.constroi_objetos(dados)

    def constroi_objetos(self, dados_tratados):
        paciente = Paciente()
        endereco = Endereco()
        exame = Teste()
        for x in range(len(dados_tratados['hits']['hits'])):

            paciente.set_paciente_idade(
                dados_tratados['hits']['hits'][x]['_source']['idade'])
            paciente.set_paciente_cbo(
                dados_tratados['hits']['hits'][x]['_source']['cbo'])
            paciente.set_paciente_sexo(
                dados_tratados['hits']['hits'][x]['_source']['sexo'])
            paciente.set_paciente_profissional_de_saude(
                dados_tratados['hits']['hits'][x]['_source']['profissionalSaude'])

            try:
                paciente.set_raca(
                    dados_tratados['hits']['hits'][x]['_source']['racaCor'])
            except KeyError:
                paciente.set_raca('indefinido')

                # construcao do OBJ ENDERECO
            endereco.set_estado(
                dados_tratados['hits']['hits'][x]['_source']['estado'])
            endereco.set_municipio(
                dados_tratados['hits']['hits'][x]['_source']['municipio'])

            try:
                # construcao do OBJ EXAME
                exame.set_data_teste(
                    dados_tratados['hits']['hits'][x]['_source']['dataTeste'])
                # exame.set_data_encerramento(
                # dados_tratados['hits']['hits'][x]['_source']['dataEncerramento'])
                exame.set_data_notificacao(
                    dados_tratados['hits']['hits'][x]['_source']['dataNotificacao'])

                exame.set_resultado(
                    dados_tratados['hits']['hits'][x]['_source']['resultadoTeste'])

                exame.set_sintomas(
                    dados_tratados['hits']['hits'][x]['_source']['sintomas'])
                exame.set_data_inicio_sintomas(
                    dados_tratados['hits']['hits'][x]['_source']['dataInicioSintomas'])
                exame.set_estado_teste(
                    dados_tratados['hits']['hits'][x]['_source']['estadoTeste'])
                exame.set_condicoes(
                    dados_tratados['hits']['hits'][x]['_source']['condicoes'])
                exame.set_evolucao(
                    dados_tratados['hits']['hits'][x]['_source']['evolucaoCaso'])

            except KeyError:
                exame.set_evolucao('curado')

            try:
                exame.set_classificacao(
                    dados_tratados['hits']['hits'][x]['_source']['classificacaoFinal'])
            except KeyError:
                exame.set_classificacao('indefinido')

            # paciente.set_dados_teste(dados_tratados[x]['teste'])

            self.insert_dados(paciente, endereco, exame)

    def insert_dados(self, paciente=Paciente(), endereco_API=Endereco(), exame=Teste()):
        
        cursor = self._con.cursor(buffered=True)
        query_insert = "INSERT INTO paciente(paciente_cbo, paciente_idade, paciente_sexo, paciente_fk_endid , paciente_profissional_de_saude, paciente_raca) VALUES(%s,%s,%s,%s,%s,%s);"

        paciente_cbo = paciente.get_paciente_cbo()
        if(paciente_cbo is None):
            paciente_cbo = 'não possui'

        idade = paciente.get_paciente_idade()
        sexo = paciente.get_paciente_sexo()
        endereco = self.insert_into_endereco(endereco_API)

        profissional_saude = paciente.get_paciente_profissional_de_saude()
        raca = paciente.get_raca()
        val = (paciente_cbo, idade, sexo, endereco, profissional_saude, raca)
        cursor.execute(query_insert, val)
        last_id = cursor.lastrowid
        self.insert_into_teste(exame, last_id)

        if(last_id < 0):
            print('ENTREI DENTRO DO IF')

        else:
            print('QUERY EXECUTADA COM SUCESSO')
            self._count=self._count +1
            if(self._count==10000):
                self._count=0
                self.get_dados_service()
    def insert_into_endereco(self, endereco=Endereco()):
        cursor = self._con.cursor(buffered=True)

        query_insert = "INSERT INTO endereco(end_municipio, end_estado) VALUES(%s,%s);"
        municipio = endereco.get_municipio()
        estado = endereco.get_estado()
        val = (municipio, estado)

        cursor.execute(query_insert, val)

        last_id = cursor.lastrowid
        self._con.commit()

        if(last_id > 0):
            print('ENDERECO INSERIDO COM SUCESSO!!!')
            return last_id
        else:
            print('ERRO AO INSERIR ENDERECO')
        return last_id

    def insert_into_teste(self, exame=Teste(), id=0):
        cursor = self._con.cursor(buffered=True)
        d = TratarData()
        query_insert = """INSERT INTO exame(ex_dt_notificacao, ex_dt_encerramento, ex_dt_coleta_teste,
                        ex_dt_ini_sintomas,ex_sintomas, ex_classificacao,
                        ex_resultado, ex_estado_teste, ex_condicoes, ex_fk_paciente_id,
                        ex_evolucao_caso) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        # print("ESSE É O Valor do Teste", teste)

        data_teste = d.convert_data(exame.get_data_teste())
        data_notificacao = d.convert_data(exame.get_data_notificacao())
        # data_encerramento = d.convert_data(exame.get_data_encerramento())
        data_ini_sintomas = d.convert_data(exame.get_data_inicio_sintomas())
        sintomas = exame.get_sintomas()
        classificacao = exame.get_classificacao()
        estado_teste = exame.get_estado_teste()
        condicoes = exame.get_condicoes()
        evolucao = exame.get_evolucao()  # teste['evolucao_caso']
        paciente = id
        resultado = exame.get_resultado()
        print(resultado)
        val = (data_notificacao, '2020-04-01',
               data_teste, data_ini_sintomas, sintomas, 'default', resultado, estado_teste, condicoes, paciente, evolucao)

        cursor.execute(query_insert, val)
        last_id = cursor.lastrowid
        self._con.commit()

        print('ESSE É O LAST ID', last_id)
        if(last_id > 0):
            print('TESTE INSERIDO COM SUCESSO!!!')
            return last_id
        else:
            print('ERRO AO INSERIR TESTE')
        return last_id


    '''def iniciar(self):
        while(True):
            self.persistir()
            time.sleep(65)'''

i= InsereBD()
t1 = threading.Thread(target=i.get_dados_service())  
t1.start()
