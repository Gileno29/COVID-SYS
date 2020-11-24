from TratarDados.TratarDados import TratarDados
from TratarDados.timer import Timer
from persistencia.conexao import Conexao
from entities.Paciente import Paciente


class AuxPersistir():

    def __init__(self):
        # Thread.__init__(self)
        '''self._paciente = TratarDados()
        self._dados = Timer()
        self._con = ConexaoBD()'''
        self._paciente = Paciente()
        self._con = Conexao.Conexao().conectar()
        self._t = Timer.Timer()

    def persistir_paciente(self):
        self._t.start()  # inicia a thread do timer
        dados = self._t.get_dados()

        dados_t = TratarDados()
        dados_paciente = dados_t.ObterDadosPaciente(dados)

        # constroi o Objeto e persiste seus menbros no BD
        self.constroi_objeto(dados_paciente)

    def constroi_objeto(self, dados_tratados):
        paciente = Paciente()

        for x in range(len(dados_tratados)):
            paciente.set_endereco(dados_tratados[x]['endereco'])
            paciente.set_idade(dados_tratados[x]['idade'])
            paciente.set_source_id(dados_tratados[x]['id'])
            paciente.set_sexo(dados_tratados[x]['sexo'])
            paciente.set_sintomas(dados_tratados[x]['sintomas'])
            paciente.set_resultado_teste(dados_tratados[x]['teste'])

            self.insert_into_paciente(paciente)

    def insert_into_paciente(self, paciente=Paciente()):
        cursor = self._con.cursor(buffered=True)
        query_insert = "INSERT INTO paciente(source_id, idade,sexo, endereco, teste, sintomas ) VALUES(%s,%s,%s,%s,%s,%s);"
        sourc = paciente.get_source_id()
        idade = paciente.get_idade()
        sexo = paciente.get_sexo()
        endereco = self.insert_into_endereco(paciente)
        teste = self.insert_into_teste(paciente)
        sintomas = paciente.get_sintomas()

        val = (sourc, idade, sexo, endereco, teste, sintomas)
        print('ESSE É O RESULTADO DO VAL ', val)
        cursor.execute(query_insert, val)

        last_id = cursor.lastrowid

        if(last_id < 0):
            print('ENTREI DENTRO DO IF')

        else:
            print('QUERY EXECUTADA COM SUCESSO')

    def insert_into_endereco(self, paciente=Paciente()):
        cursor = self._con.cursor(buffered=True)

        query_insert = "INSERT INTO endereco(municipio, estado) VALUES(%s,%s);"

        endereco = paciente.get_endereco()

        for x in range(len(endereco)):

            municipio = endereco['municipio']
            estado = endereco['estado']
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

    def insert_into_teste(self, paciente=Paciente()):
        cursor = self._con.cursor(buffered=True)
        query_insert = """INSERT INTO teste(data_teste, data_notificacao, resultado) VALUES(%s,%s,%s)"""

        teste = paciente.get_resultado_teste()

        for x in range(len(teste)):
            data_teste = teste['data_teste']
            data_notificacao = teste['data_notificacao']
            resultado = teste['resultado']
            val = (data_teste, data_notificacao, resultado)

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


ax = AuxPersistir()
ax.persistir_paciente()
