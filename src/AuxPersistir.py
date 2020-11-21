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

            self.insert_into_paciente(paciente)
            # print(paciente)
            # print(paciente)
            # if(x == len(dados_tratados['hits']['hits'])):
            # break

    def insert_into_paciente(self, paciente=Paciente()):
        query_create = "CREATE TABLE IF NOT EXISTS paciente(id int(11) AUTO_INCREMENT NOT NULL ,source_id varchar(20)NOT NULL,idade int(11), sexo VARCHAR(12), endereco int(12), PRIMARY KEY(id), FOREIGN KEY (endereco) REFERENCES endereco(id));"
        cursor = self._con.cursor()
        query_insert = "INSERT INTO paciente(municipio, estado) VALUES(%s,%s,%s);"
        sourc = paciente.get_source_id()
        idade = paciente.get_idade()
        sexo = paciente.get_sexo()

        # print(sexo)
        val = (sourc, idade, sexo)

        rows = cursor.execute(query_create)

        if(rows < 0):
            print('ENTREI DENTRO DO IF')
            self.insert_into_endereco(paciente)

        else:
            print('QUERY EXECUTADA COM SUCESSO')
        cursor.execute(query_insert, val)

    def insert_into_endereco(self, paciente=Paciente()):
        query_create = "CRETE TABLE [IF NOT EXISTS] endereco(id int(11) AUTO_INCREMENT NOT NULL, municipio varchar(15), estado varchar(15), PRIMARY KEY(id));"
        query_insert = "INSERT INTO endereco(municipio, estado) VALUES(%s,%s);"

        endereco = paciente.get_endereco()

        for x in range(len(endereco)):
            pass
        '''
        val = (municipio, estado)
        cursor = self._con.cursor()
        cursor.execute(query_create)
        cursor.execute(query_insert, val)
        '''


ax = AuxPersistir()
ax.persistir_paciente()
