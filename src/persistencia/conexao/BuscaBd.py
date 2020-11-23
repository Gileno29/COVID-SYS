from ConexaoBD import conexao


class BuscaBD():

    def __init__(self):
        self._con = conexao()

    def buscar_paciente(self, id=0):
        identificador = id
        conect = self._con.conectar()

        cursor = conect.cursor(buffered=True)

        query_select_paciente = '''SELECT * FROM paciente; '''
        query_select_by_id = "SELECT * FROM paciente WHERE id= %s;"

        if (id != 0):

            val = (identificador,)
            cursor.execute(query_select_by_id, val)

            result_paciente = cursor.fetchone()
            return result_paciente
        else:
            cursor.execute(query_select_paciente)

            result = cursor.fetchall()
            print(result)

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


con = BuscaBD()

con.buscar_paciente(55)
