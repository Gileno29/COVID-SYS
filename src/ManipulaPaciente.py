from Paciente import Paciente
from GerenciaServices import GerenciaServices


class ManipulaPaciente:

    def __init__(self):
        pass

    def cria_paciente(self, paciente):
        # print(paciente)

        p1 = Paciente()
        for x in range(len(paciente)):
            # print(paciente[x])
            print(x)
            p1.set_source_id(paciente[x]['source_id'])
            p1.set_municipio(paciente[x]['municipio'])
            p1.set_estado(paciente[x]['estado'])

        print('dados ', p1.get_estado(), p1.get_municipio(), p1.get_source_id())
        # print(paciente)

    def agrupaPaciente(self):
        service = GerenciaServices()

        dados = service.get_dados_service()

        pacientes = service.get_info(dados)

        for x in range(len(pacientes)):
            paciente = []
            if x > 4:
                continue

            paciente.append(pacientes[x])

            self.cria_paciente(paciente)


m = ManipulaPaciente()

m.agrupaPaciente()
