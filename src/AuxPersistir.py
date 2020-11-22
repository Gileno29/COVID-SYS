from threading import Thread
from TratarDados.TratarDados import TratarDados
from TratarDados.timer import Timer
from persistencia.conexao import ConexaoBD
from entities.Paciente import Paciente


class AuxPersistir():

    def __init__(self):
        # Thread.__init__(self)
        '''self._paciente = TratarDados()
        self._dados = Timer()
        self._con = ConexaoBD()'''
        self._paciente = Paciente()
        self._con = ConexaoBD.conexao().conectar()
        self._t = Timer.Timer()

    def persistir_paciente(self):
        # con = ConexaoBD()
        self._t.start()  # inicia a thread do timer
        dados = self._t.get_dados()

        dados_t = TratarDados()
        dados_paciente = dados_t.ObterDadosPaciente(dados)
        self.constroi_objeto(dados_paciente)

    def constroi_objeto(self, dados_tratados):
        paciente = Paciente()
        # print(dados_tratados)

        for x in range(len(dados_tratados)):
            paciente.set_endereco(dados_tratados[x]['endereco'])
            paciente.set_idade(dados_tratados[x]['idade'])
            paciente.set_source_id(dados_tratados[x]['id'])
            paciente.set_sexo(dados_tratados[x]['sexo'])
            paciente.set_sintomas(dados_tratados[x]['sintomas'])
            paciente.set_resultado_teste(dados_tratados[x]['teste'])

            self.insert_into_paciente(paciente)
            # print(paciente)
            # print(paciente)
            # if(x == len(dados_tratados['hits']['hits'])):
            # break

    def insert_into_paciente(self, paciente=Paciente()):
        # query_create = "CREATE TABLE IF NOT EXISTS paciente(id int(11) AUTO_INCREMENT NOT NULL ,source_id varchar(20)NOT NULL,idade int(11), sexo VARCHAR(12), endereco int(12), PRIMARY KEY(id), FOREIGN KEY (endereco) REFERENCES endereco(id));"
        cursor = self._con.cursor(buffered=True)
        query_insert = "INSERT INTO paciente(source_id, idade,sexo, endereco, teste, sintomas ) VALUES(%s,%s,%s,%s,%s,%s);"
        sourc = paciente.get_source_id()
        idade = paciente.get_idade()
        sexo = paciente.get_sexo()
        endereco = self.insert_into_endereco(paciente)
        teste = self.insert_into_teste(paciente)
        sintomas = paciente.get_sintomas()

        # print(sexo)
        val = (sourc, idade, sexo, endereco, teste, sintomas)
        print('ESSE É O RESULTADO DO VAL ', val)
        rows = cursor.execute(query_insert, val)

        if(rows < 0):
            print('ENTREI DENTRO DO IF')

        else:
            print('QUERY EXECUTADA COM SUCESSO')

    def insert_into_endereco(self, paciente=Paciente()):
        cursor = self._con.cursor(buffered=True)

        query_insert = "INSERT INTO endereco(municipio, estado) VALUES(%s,%s);"
        query_last_id = "SELECT LAST_INSERT_ID();"

        endereco = paciente.get_endereco()

        for x in range(len(endereco)):
            #print('PRINT DO ENDERECO ', endereco['estado'])
            municipio = endereco['municipio']
            estado = endereco['estado']
            val = (municipio, estado)
            #print('RESULTADO DE VALL ENDERECO', val)
            cursor.execute(query_insert, val)

            last_id = cursor.execute(query_last_id)
            #print('ESSE É O PRINT DO LAST ID', last_id)

            if(last_id):
                print('ENDERECO INSERIDO COM SUCESSO!!!')
                return last_id
            else:
                print('ERRO AO INSERIR ENDERECO')
            return last_id
        '''
        val = (municipio, estado)
        cursor = self._con.cursor()
        cursor.execute(query_create)
        cursor.execute(query_insert, val)
        '''

    def insert_into_teste(self, paciente=Paciente()):
        cursor = self._con.cursor(buffered=True)
        query_insert = """INSERT INTO teste(data_teste, data_notificacao, resultado) VALUES(%s,%s,%s)"""
        query_last_id = """SELECT LAST_INSERT_ID();"""

        teste = paciente.get_resultado_teste()

        for x in range(len(teste)):
            data_teste = teste['data_teste']
            data_notificacao = teste['data_notificacao']
            resultado = teste['resultado']
            val = (data_teste, data_notificacao, resultado)

           #print('ESSE É O VAL DE TESTE', val)

            cursor.execute(query_insert, val)
            #cursor.execute("create table debug(teste varchar(15));")
            last_id = cursor.execute(query_last_id)
            self._con.commit()
            resultado = cursor.fetchone()
            print('ESSE É O LAST ID', last_id)
            if(resultado):
                print('TESTE INSERIDO COM SUCESSO!!!')
                return last_id
            else:
                print('ERRO AO INSERIR TESTE')
            return last_id


ax = AuxPersistir()
ax.persistir_paciente()
