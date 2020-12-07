from persistencia.conexao import Conexao
import datetime


class BuscaBD:

    def __init__(self):
        self._con = Conexao.Conexao()

    def buscar_paciente(self, id=0):
        identificador = id
        conect = self._con.conectar()

        cursor = conect.cursor(buffered=True)
        query_select_by_id = "SELECT * FROM paciente WHERE id= %s;"
        query_select_paciente = "SELECT p.paciente_cbo, p.paciente_sexo, p.paciente_idade, e.end_municipio, e.end_estado, ex.ex_dt_notificacao, ex.ex_dt_ini_sintomas, ex.ex_resultado  FROM endereco as e, paciente as p, exame as ex  where e.end_id= p.paciente_fk_endid AND ex. ex_fk_paciente_id=p.paciente_id;"

        if (id != 0):

            val = (identificador,)
            cursor.execute(query_select_by_id, val)

            result_paciente = cursor.fetchone()

            '''result_endereco = self.buscar_endereco(id)
            result_teste = self.buscar_teste(id)'''
            result_paciente
            return result_paciente
        else:
            cursor.execute(query_select_paciente)

            result = cursor.fetchall()
            # print(result)
            result

            # print(result2)

            return result

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

    '''def convet_to_json(self, result):
        obj = '{' + ', '.join('"{}": "{}"'.format(k, v)
                              for k, v in result) + '}'
        print(obj)'''


"""
con = BuscaBD()
con.buscar_paciente()
"""
