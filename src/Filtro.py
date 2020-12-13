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

    def buscar_obtos_sintomas(self):
        conect = self._con.conectar()
        cursor = conect.cursor(buffered=True)
        query_select_paciente = "SELECT  p.paciente_sexo, ex.ex_sintomas, ex.ex_resultado, ex.ex_evolucao_caso FROM  paciente as p, exame as ex  where ex. ex_fk_paciente_id=p.paciente_id;"

        cursor.execute(query_select_paciente)
        result = cursor.fetchall()
        return result

    def calcula_morte_sexo(self):
        h = 0
        m = 0
        dados = self._busca.buscar_paciente_sexo()

        for x in range(len(dados)):
            if(dados[x][0] == "Feminino" and dados[x][1] == "Óbito" and dados[x][2] == "Positivo"):
                m = m+1
            elif(dados[x][0] == "Masculino" and dados[x][1] == "Óbito" and dados[x][2] == "Positivo"):
                h = h+1

        total = {'mulher': m, 'homem': h}

        return total

    def calcula_morte_sintomas(self):
        dados = self._busca.buscar_obtos_sintomas()
        febre = 0
        tosse = 0
        dor_garganta = 0
        dispineia = 0
        outros = 0
        # print(dados)
        for x in range(len(dados)):
            if(dados[x][2] == "Positivo" and dados[x][3] == "Óbito"):
                dados_novos = dados[x][1].split(",")

                if("Dor de Garganta" in dados_novos):
                    dor_garganta = dor_garganta + 1
                    if("Tosse" in dados_novos):
                        tosse = tosse + 1
                    elif("Febre" in dados_novos):
                        febre = febre + 1
                    elif("Dispineia" in dados_novos):
                        dispineia = dispineia + 1
                    elif("Outros" in dados_novos):
                        outros = outros + 1

                if("Tosse" in dados_novos):
                    tosse = tosse + 1
                    if("Dor de Garganta" in dados_novos):
                        dor_garganta = dor_garganta + 1
                    elif("Febre" in dados_novos):
                        febre = febre + 1
                    elif("Dispineia" in dados_novos):
                        dispineia = dispineia + 1
                    elif("Outros" in dados_novos):
                        outros = outros + 1

                if("Dispneia" in dados_novos):
                    dispineia = dispineia + 1
                    if("Dor de Garganta" in dados_novos):
                        dor_garganta = dor_garganta + 1
                    elif("Tosse" in dados_novos):
                        tosse = tosse + 1
                    elif("Febre" in dados_novos):
                        febre = febre + 1
                    elif("Outros" in dados_novos):
                        outros = outros + 1

                if("Outros" in dados_novos):
                    outros = outros + 1
                    if("Dor de Garganta" in dados_novos):
                        dor_garganta = dor_garganta + 1
                    elif("Tosse" in dados_novos):
                        tosse = tosse + 1
                    elif("Febre" in dados_novos):
                        febre = febre + 1
                    elif("Dispineia" in dados_novos):
                        dispineia = dispineia + 1

                if("Febre" in dados_novos):
                    febre = febre + 1
                    if("Dor de Garganta" in dados_novos):
                        dor_garganta = dor_garganta + 1
                    elif("Tosse" in dados_novos):
                        tosse = tosse + 1
                    elif("Outros" in dados_novos):
                        outros = outros + 1
                    elif("Dispineia" in dados_novos):
                        dispineia = dispineia + 1

        total = {'febre': febre, 'dor_garganta': dor_garganta,
                 'tosse': tosse, 'dispineia': dispineia, 'outros': outros}

        return total


f = Filtro()

f.calcula_morte_sintomas()
