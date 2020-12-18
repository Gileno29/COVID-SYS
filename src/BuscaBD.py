from persistencia.conexao import Conexao
import datetime


class BuscaBD:

    def __init__(self):
        self._con = Conexao.Conexao()
        self._paciente = object
        self._endereco = object
        self._exame = object

    def buscar_paciente(self, id=0):
        identificador = id
        conect = self._con.conectar()
        cursor = conect.cursor(buffered=True)
        query_select_by_id = "SELECT * FROM paciente WHERE paciente_id= %s;"
        query_select_end_by_id = "SELECT e.end_id, e.end_estado, e.end_municipio, p.paciente_id from endereco as e, paciente as p where p.paciente_fk_endid= e.end_id and e.end_id=%s;"

        query_select_paciente = "SELECT p.paciente_id, p.paciente_cbo, p.paciente_sexo, p.paciente_idade, e.end_municipio, e.end_estado, ex.ex_dt_notificacao, ex.ex_dt_ini_sintomas, ex.ex_resultado  FROM endereco as e, paciente as p, exame as ex  where e.end_id= p.paciente_fk_endid AND ex. ex_fk_paciente_id=p.paciente_id;"

        query_select_ALL = "SELECT p.paciente_id, p.paciente_cbo, p.paciente_sexo, p.paciente_idade,p.paciente_profissional_de_saude,p.paciente_raca, e.end_id, e.end_estado, e.end_municipio from paciente as p, endereco as e where p.paciente_fk_endid= e.end_id"

        paciente = {'id': '', 'cbo': '', 'sexo': '', 'idade': 0,
                    'profissional_de_saude': '', 'profissional_seguranca': '',
                    'raca': '', 'endereco': {'end_id': '', 'estado': '', 'municipio': ''}}

        paciente_result = []
        end_result = []
        if (id != 0):

            val = (identificador,)
            cursor.execute(query_select_by_id, val)
            paciente_result = cursor.fetchone()

            cursor.execute(query_select_end_by_id, val)
            end_result = cursor.fetchone()

            paciente = {'id': paciente_result[0], 'cbo': paciente_result[1], 'sexo': paciente_result[2],
                        'idade': paciente_result[3], 'profissional_de_saude': paciente_result[4],
                        'profissional_seguranca': paciente_result[5], 'raca': paciente_result[6],
                        'endereco': {'end_id': end_result[0], 'estado': end_result[1], 'muncipio': end_result[2]}}

            return paciente
        else:

            cursor.execute(query_select_ALL)
            paciente_result = cursor.fetchall()
            pacientes = []
            p = {}
            for x in range(len(paciente_result)):
                #print(len(paciente_result))
                #print(paciente_result)
                p = {'id': paciente_result[x][0], 'cbo': paciente_result[x][1], 'sexo': paciente_result[x][2],
                     'idade': paciente_result[x][3], 'profissional_de_saude': paciente_result[x][4], 'raca': paciente_result[x][5],
                     'end_id': paciente_result[x][6], 'estado': paciente_result[x][7], 'muncipio': paciente_result[x][8]}
                pacientes.append(p)
            return pacientes

    def buscar_endereco(self, id_endereco=0, id_paciente=0):
        conect = self._con.conectar()

        cursor = conect.cursor(buffered=True)

        query_select_endereco = '''SELECT * FROM endereco; '''
        query_select_by_id = "SELECT * FROM endereco WHERE id= %s;"

        if(id_endereco != 0):
            val = (id,)
            cursor.execute(query_select_by_id, val)
            result = cursor.fetchone()

            return result
        else:
            cursor.execute(query_select_endereco)
            result = cursor.fecthall()

            return result

    def buscar_teste(self, id=0):
        conect = self._con.conectar()
        cursor = conect.cursor(buffered=True)
        query_select_teste = '''SELECT * FROM teste; '''
        query_select_by_id = "SELECT * FROM endereco WHERE id= %s;"

        if(id != 0):
            val = (id,)
            cursor.execute(query_select_by_id, val)

            result = cursor.fecthone()

            return result
        else:
            cursor.excute(query_select_teste)

            result = cursor.fetchone()

            return result

    def mapeamento(self, paciente={}, endereco={}, teste={}):

        for x in range(len(paciente)):
            paciente = {paciente}
            pass
        pass

    def buscar_paciente_sexo(self, estado=None):
        conect = self._con.conectar()
        cursor = conect.cursor(buffered=True)
        query_select_paciente = ''
        result = []
        if(estado is not None):
            estados = {'RN': 'Rio Grande Do Norte', 'AC': 'Acre'}
            if(estado in estados):
                val = (estados[estado],)
                query_select_paciente = "SELECT  p.paciente_sexo, ex.ex_evolucao_caso, ex_resultado, e.end_estado FROM  paciente as p, exame as ex, endereco as e  where ex.ex_fk_paciente_id = p.paciente_id and e.end_estado like %s and p.paciente_fk_endid = end_id limit 6000"
                cursor.execute(query_select_paciente, val)
                result = cursor.fetchall()
        else:
            query_select_paciente = "SELECT  p.paciente_sexo, ex.ex_evolucao_caso, ex_resultado FROM  paciente as p, exame as ex where ex. ex_fk_paciente_id=p.paciente_id;"
            cursor.execute(query_select_paciente)
            result = cursor.fetchall()

        return result

    def buscar_obtos_sintomas(self, estado=None):
        conect = self._con.conectar()
        query_select_paciente = ''
        result = []
        if(estado is not None):
            estados = {'RN': 'Rio Grande Do Norte', 'AC': 'Acre'}
            if(estado in estados):
                
                val = (estados[estado],)
                query_select_paciente = "SELECT  p.paciente_sexo, ex.ex_sintomas, ex.ex_resultado, ex.ex_evolucao_caso, e.end_estado FROM  paciente as p, exame as ex, endereco as e  where ex. ex_fk_paciente_id=p.paciente_id and e.end_estado like %s and p.paciente_fk_endid = end_id limit 6000;"
                cursor = conect.cursor(buffered=True)
                cursor.execute(query_select_paciente, val)
                result = cursor.fetchall()
            else:
                pass
               
        else:
            query_select_paciente = "SELECT  p.paciente_sexo, ex.ex_sintomas, ex.ex_resultado, ex.ex_evolucao_caso FROM  paciente as p, exame as ex  where ex. ex_fk_paciente_id=p.paciente_id;"
            cursor = conect.cursor(buffered=True)
            cursor.execute(query_select_paciente)
            result = cursor.fetchall()

        return result

    def buscar_obtos_idade(self, estado=None):
        conect = self._con.conectar()
        cursor = conect.cursor(buffered=True)
        query_select_paciente = ''
        result = []
        if(estado is not None):
            estados = {'RN': 'Rio Grande Do Norte', 'AC': 'Acre'}
            if(estado in estados):
                val = (estados[estado],)
                query_select_paciente = "SELECT  p.paciente_idade, ex.ex_evolucao_caso, ex_resultado, e.end_estado FROM  paciente as p, exame as ex, endereco as e  where ex.ex_fk_paciente_id = p.paciente_id and e.end_estado like %s and p.paciente_fk_endid = end_id limit 6000"
                cursor.execute(query_select_paciente, val)
                result = cursor.fetchall()
        else:
            query_select_paciente = "SELECT  p.paciente_idade, ex.ex_evolucao_caso, ex_resultado FROM  paciente as p, exame as ex where ex. ex_fk_paciente_id=p.paciente_id;"
            cursor.execute(query_select_paciente)
            result = cursor.fetchall()

        return result

    def buscar_infectados(self):
        query = "select ex.ex_resultado from exame as ex where ex.ex_resultado like '%Positivo%'; "
        conect = self._con.conectar()
        cursor = conect.cursor(buffered=True)
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    def buscar_obtos(self):
        query = "select ex.ex_resultado, ex.ex_evolucao_caso from exame as ex where ex.ex_evolucao_caso like '%Óbito%'; "
        conect = self._con.conectar()
        cursor = conect.cursor(buffered=True)
        cursor.execute(query)
        result = cursor.fetchall()

        return result
    def buscar_infectados_estado(self, estado='Rio Grande Do Norte'):
        
        query = "SELECT  p.paciente_id, ex.ex_evolucao_caso, ex.ex_resultado,ex.ex_dt_encerramento, e.end_estado FROM  paciente as p, exame as ex, endereco as e  where ex.ex_fk_paciente_id = p.paciente_id and e.end_estado like %s and p.paciente_fk_endid = end_id; "
        conect = self._con.conectar()
        cursor = conect.cursor(buffered=True)
        val=(estado,)
        result=[]
        if(estado!='Rio Grande Do Norte'):
                estados = {'RN': 'Rio Grande Do Norte',
                       'AC': 'Acre', 'SP': 'Sao Paulo', 'PB': 'Paraiba'}
                if(estado in estados):
                    val = (estados[estado],)
                    query = "SELECT  p.paciente_id, ex.ex_evolucao_caso, ex.ex_resultado, ex.ex_dt_encerramento, p.paciente_id, e.end_estado FROM  paciente as p, exame as ex, endereco as e  where ex.ex_fk_paciente_id = p.paciente_id and e.end_estado like %s and p.paciente_fk_endid = end_id; "
                    cursor.execute(query, val)
                    result = cursor.fetchall()
        else:

            cursor.execute(query, val)
            result = cursor.fetchall()
        
        return result
    def buscar_obtos_mes(self, estado=None):
        query = ""
        conect = self._con.conectar()
        cursor = conect.cursor(buffered=True)
        result = []
        if(estado is not None):
            estados = {'RN': 'Rio Grande Do Norte',
                       'AC': 'Acre', 'SP': 'Sao Paulo', 'PB': 'Paraiba'}
            if(estado in estados):
                val = (estados[estado],)
                query = "SELECT  ex.ex_resultado, ex.ex_evolucao_caso, ex.ex_dt_encerramento, p.paciente_id, e.end_estado FROM  paciente as p, exame as ex, endereco as e  where ex.ex_fk_paciente_id = p.paciente_id and e.end_estado like %s and p.paciente_fk_endid = end_id; "
                cursor.execute(query, val)
                result = cursor.fetchall()
        else:
            query = "select ex.ex_resultado, ex.ex_evolucao_caso, ex_dt_encerramento from exame as ex where ex.ex_resultado like '%Positivo%'; "
            cursor.execute(query)
            result = cursor.fetchall()

        return result

    def buscar_obtos_raca(self, estado=None):
        query = ""
        conect = self._con.conectar()
        cursor = conect.cursor(buffered=True)
        result = []
        if(estado is not None):
            estados = {'RN': 'Rio Grande Do Norte',
                       'AC': 'Acre', 'SP': 'Sao Paulo', 'PB': 'Paraiba'}
            if(estado in estados):
                val = (estados[estado],)
                query = "SELECT  p.paciente_raca,  ex.ex_resultado, ex.ex_evolucao_caso, e.end_estado FROM  paciente as p, exame as ex, endereco as e  where ex.ex_fk_paciente_id = p.paciente_id and e.end_estado like %s and p.paciente_fk_endid = end_id; "
                cursor.execute(query, val)
                result = cursor.fetchall()
        else:
            query = "select p.paciente_raca, ex.ex_resultado, ex.ex_evolucao_caso from paciente as p, exame as ex where ex.ex_fk_paciente_id=p.paciente_id; "
            cursor.execute(query)
            result = cursor.fetchall()

        return result


con = BuscaBD()
con.buscar_paciente(10)
