from persistencia.conexao import Conexao
from BuscaBD import BuscaBD


class Filtro:
    def __init__(self):
        self._con = Conexao.Conexao()
        self._busca = BuscaBD()

    def buscar_paciente_sexo(self):
        conect = self._con.conectar()
        cursor = conect.cursor(buffered=True)
        query_select_paciente = "SELECT  p.paciente_sexo, ex.ex_evolucao_caso FROM  paciente as p, exame as ex  where ex. ex_fk_paciente_id=p.paciente_id;"

        cursor.execute(query_select_paciente)
        result = cursor.fetchall()
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

    def calculaMorteSexo(self):
        h = 0
        m = 0
        dados = self._busca.buscar_paciente_sexo()

        for x in range(len(dados)):
            if(dados[x][0] == "Feminino" and dados[x][1] == "Óbito" and dados[x][2]):
                m = m+1
            elif(dados[x][0] == "Masculino" and dados[x][1] == "Óbito" and dados[x][2]):
                h = h+1

        total = {'mulher': m, 'homem': h}

        return total


f = Filtro()

f.calculaMorteSexo()
