from Paciente import Paciente
from GerenciaServices import GerenciaServices


class ManipulaPaciente:

    def __init__(self):
        pass

    def persiste_paciente(self):

        service = GerenciaServices()

        dados = service.get_dados_service()

        paciente = service.get_info(dados)

        p1 = Paciente()

        p1.set_nome(paciente)
        nome = p1.get_nome()
        print(nome)


m = ManipulaPaciente()


m.persiste_paciente()
