from BuscaBD import BuscaBD
from datetime import datetime


class Filtro:
    def __init__(self):
        self._busca = BuscaBD()

    def buscar_obtos_sintomas(self):
        conect = self._con.conectar()
        cursor = conect.cursor(buffered=True)
        query_select_paciente = "SELECT  p.paciente_sexo, ex.ex_sintomas, ex.ex_resultado, ex.ex_evolucao_caso FROM  paciente as p, exame as ex  where ex. ex_fk_paciente_id=p.paciente_id;"

        cursor.execute(query_select_paciente)
        result = cursor.fetchall()
        return result

    def calcula_morte_sexo(self, estado=None):
        h = 0
        m = 0
        dados = []
        if(estado is not None):
            dados = self._busca.dados = self._busca.buscar_paciente_sexo(
                estado)

        else:
            dados = self._busca.buscar_paciente_sexo()

        for x in range(len(dados)):
            if(dados[x][0] == "Feminino" and dados[x][1] == "Óbito" and dados[x][2] == "Positivo"):
                m = m+1
            elif(dados[x][0] == "Masculino" and dados[x][1] == "Óbito" and dados[x][2] == "Positivo"):
                h = h+1

        total = {'mulher': m, 'homem': h}

        return total

    def calcula_morte_sintomas(self, estado=None):
        dados = []
        febre = 0
        tosse = 0
        dor_garganta = 0
        dispineia = 0
        outros = 0
        if(estado is not None):
            dados = self._busca.buscar_obtos_sintomas(estado)
           
        else:
            dados = self._busca.buscar_obtos_sintomas()
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

    def calcular_morte_por_idade(self, estado=None):
        idade0A25 = 0
        idade26A30 = 0
        idade31A40 = 0
        idade41A60 = 0
        maisDe60 = 0
        total = []
        if(estado is not None):
            dados = self._busca.buscar_obtos_idade(estado)
        else:
            dados = self._busca.buscar_obtos_idade()
        for x in range(len(dados)):
            if(dados[x][2] == "Positivo" and dados[x][1] == "Óbito"):

                if(dados[x][0] <= 25):
                    idade0A25 = idade0A25 + 1
                elif(dados[x][0] > 25 and dados[x][0] < 31):
                    idade26A30 = idade26A30 + 1
                elif(dados[x][0] > 30 and dados[x][0] < 40):
                    idade31A40 = idade31A40 + 1
                elif(dados[x][0] > 40 and dados[x][0] < 60):
                    idade41A60 = idade41A60 + 1
                else:
                    maisDe60 = maisDe60+1

        total = {'idade0A25': idade0A25, 'idade26A30': idade26A30,
                 'idade31A40': idade31A40, 'idade41A60': idade41A60, 'maisDe60': maisDe60}

        return total

    def quantidade_infectados(self):
        total = {}
        infectados = 0
        dados = self._busca.buscar_infectados()

        for x in range(len(dados)):

            if(dados[x][0] == "Positivo"):
                infectados = infectados + 1

        total = {'infectados': infectados}
        return total

    def quantidade_obtos(self):
        total = {}
        obito = 0
        dados = self._busca.buscar_obtos()

        for x in range(len(dados)):

            if(dados[x][1] == "Óbito" and dados[x][0] == "Positivo"):
                obito = obito + 1

        total = {'obitos': obito}
        return total

    def quantidade_obtos_mes(self, estado=None):
        total = {}
        janeiro = 0
        fevereiro = 0
        marco = 0
        abril = 0
        maio = 0
        junho = 0
        julho = 0
        agosto = 0
        setembro = 0
        outubro = 0
        novembro = 0
        dezembro = 0
        dados = []
        
        if(estado is not None):
            dados = self._busca.buscar_obtos_mes(estado)
        else:
            dados = self._busca.buscar_obtos_mes()

        for x in range(len(dados)):

            if(dados[x][0] == "Positivo" and dados[x][1] == "Óbito"):
                data_str = dados[x][2].strftime("%Y-%m-%d")
                data_list = data_str.split('-')
                if(data_list[1] == '01'):
                    janeiro = janeiro + 1

                elif(data_list[1] == '02'):
                    fevereiro = fevereiro + 1

                elif(data_list[1] == '03'):
                    marco = marco + 1

                elif(data_list[1] == '04'):
                    abril = abril + 1

                elif(data_list[1] == '05'):
                    maio = maio + 1

                elif(data_list[1] == '06'):
                    junho = junho + 1

                elif(data_list[1] == '07'):
                    julho = julho + 1

                elif(data_list[1] == '08'):
                    agosto = agosto + 1

                elif(data_list[1] == '09'):
                    setembro = setembro + 1

                elif(data_list[1] == '10'):
                    outubro = outubro + 1

                elif(data_list[1] == '11'):
                    novembro = novembro + 1

                elif(data_list[1] == '12'):
                    dezembro = dezembro + 1

                

        total = {'janeiro': janeiro, 'fevereiro': fevereiro, 'marco': marco, 'abril':
                 abril, 'maio': maio, 'junho': junho, 'julho': julho, 'agosto': agosto,
                 'setembro': setembro, 'outubro': outubro, 'novembro': novembro, 'dezembro': dezembro}

        return total

    def calcula_obtos_raca(self, estado=None):
        parda = 0
        branca = 0
        negra = 0
        indefinida = 0
        total = {}
        if(estado is not None):
            dados = self._busca.buscar_obtos_raca(estado)
        else:
            dados = self._busca.buscar_obtos_raca()
        for x in range(len(dados)):
            if(dados[x][1] == "Positivo" and dados[x][2] == "Óbito"):

                if(dados[x][0] == "Parda"):
                    parda = parda + 1
                elif(dados[x][0] == "Branca"):
                    branca = branca + 1
                elif(dados[x][0] == "Preta"):
                    negra = negra + 1
                elif(dados[x][0] == "Preta"):
                    indefinida = indefinida + 1

        total = {'parda': parda, 'branca': branca,
                 'negra': negra, 'indefinida': indefinida}
        return total

    def calcula_infectados_estado(self, estado='Rio Grande Do Norte'):
        dados=[]
        infectados_estado=0
        if(estado != 'Rio Grande Do Norte'):
            dados = self._busca.buscar_infectados_estado(estado)
        else:
            dados = self._busca.buscar_infectados_estado()
        for x in range(len(dados)):

            if(dados[x][2] == "Positivo"):
                infectados_estado=infectados_estado + 1
        total={'infectados_estado':infectados_estado}

        return total

    def calcula_obtos_estado(self, estado='Rio Grande Do Norte'):
        dados=[]
        obitos_estado=0
        if(estado != 'Rio Grande Do Norte'):
            dados = self._busca.buscar_obtos_estado(estado)
        else:
            dados = self._busca.buscar_obtos_estado()
        for x in range(len(dados)):

            if(dados[x][2] == "Positivo" and dados[x][1] == "Óbito"):
                obitos_estado=obitos_estado + 1
        total={'obitos_estado':obitos_estado}

        return total
        
f = Filtro()

f.calcula_infectados_estado()
