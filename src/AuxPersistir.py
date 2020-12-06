from TratarDados.TratarDados import TratarDados
from TratarDados.timer import Timer
from persistencia.conexao import Conexao
from entities.Paciente import Paciente
from datetime import datetime
from TratarData import TratarData


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
            paciente.set_paciente_endereco(dados_tratados[x]['endereco'])
            paciente.set_paciente_idade(dados_tratados[x]['idade'])
            paciente.set_paciente_cbo(dados_tratados[x]['CBO'])
            paciente.set_paciente_sexo(dados_tratados[x]['sexo'])
            paciente.set_paciente_profissional_de_saude(
                dados_tratados[x]['proficional_saude'])
            paciente.set_dados_teste(dados_tratados[x]['teste'])

            self.insert_into_paciente(paciente)

    def insert_into_paciente(self, paciente=Paciente()):
        cursor = self._con.cursor(buffered=True)
        query_insert = "INSERT INTO paciente(paciente_cbo, paciente_idade, paciente_sexo, paciente_fk_endid , paciente_profissional_de_saude) VALUES(%s,%s,%s,%s,%s);"
        paciente_cbo = paciente.get_paciente_cbo()

        if(paciente_cbo == None):
            paciente_cbo = 'não possui'

        #print('CBO', paciente_cbo)

        idade = paciente.get_paciente_idade()
        sexo = paciente.get_paciente_sexo()
        endereco = self.insert_into_endereco(paciente)
        profissional_saude = paciente.get_paciente_profissional_de_saude()

        val = (paciente_cbo, idade, sexo, endereco, profissional_saude)

        #print('ESSE É O RESULTADO DO VAL ', val)

        cursor.execute(query_insert, val)

        last_id = cursor.lastrowid
        self.insert_into_teste(paciente, last_id)

        if(last_id < 0):
            print('ENTREI DENTRO DO IF')

        else:
            print('QUERY EXECUTADA COM SUCESSO')

    def insert_into_endereco(self, paciente=Paciente()):
        cursor = self._con.cursor(buffered=True)

        query_insert = "INSERT INTO endereco(end_municipio, end_estado) VALUES(%s,%s);"
        pais = 'Brasil'
        endereco = paciente.get_paciente_endereco()

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

    def insert_into_teste(self, paciente=Paciente(), id=0):
        cursor = self._con.cursor(buffered=True)
        d = TratarData()
        query_insert = """INSERT INTO exame(ex_dt_notificacao, ex_dt_encerramento, ex_dt_coleta_teste,
                        ex_dt_ini_sintomas,ex_sintomas, ex_classificacao,  
                        ex_resultado, ex_estado_teste, ex_condicoes, ex_fk_paciente_id,
                        ex_evolucao_caso) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        teste = paciente.get_dados_teste()

        print("ESSE É O Valor do Teste", teste)

        for x in range(len(teste)):
            data_teste = d.convert_data(teste['data_teste'])
            data_notificacao = d.convert_data(teste['data_notificacao'])
            data_encerramento = d.convert_data(teste['data_encerramento'])
            data_ini_sintomas = d.convert_data(teste['data_inicio_sintomas'])
            sintomas = teste['sintomas']
            classificacao = teste['classificacao']
            estado_teste = teste['estado_teste']
            condicoes = teste['condicoes']
            evolucao = teste['evolucao_caso']
            paciente = id
            resultado = teste['resultado']

            val = (data_notificacao, data_encerramento,
                   data_teste, data_ini_sintomas, sintomas, classificacao, resultado, estado_teste, condicoes, paciente, evolucao)

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
