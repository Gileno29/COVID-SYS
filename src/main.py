#from Paciente import Paciente
from GerenciaServices import GerenciaServices


class main:

    service1 = GerenciaServices()
    dados = service1.get_dados_service()
    # print(dados)
    service1.get_info(dados)
