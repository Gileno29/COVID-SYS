from conexao import ConexaoBD
from GerenciaServices import GerenciaServices


class PersistePaciente:

    def __init__(self):
        pass

    def

    def savePaciente(self):
        p = GerenciaServices()
        pacientes = p.get_dados_service()
        dados = p.get_info(pacientes)
        print(dados)

        pass


p = PersistePaciente()
p.savePaciente()
