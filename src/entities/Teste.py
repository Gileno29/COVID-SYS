class Teste:

    def __init__(self):

        self._data_teste = ''
        self._data_notificacao = ''
        self._data_encerramento = ''
        self._data_inicio_sintomas = ''
        self._sintomas = {}
        self._classificacao = ''
        self._resultado = ''
        self._estado_teste = ''
        self._condicoes = ''
        self._descr_sintomas_outros = ''
        self._paciente = ''
        self._evolucao = ''

    def set_data_teste(self, data):
        self._data_teste = data

    def get_data_teste(self):
        return self._data_teste

    def set_data_notificacao(self, data):
        self._data_notificacao = data

    def get_data_notificacao(self):
        return self._data_notificacao

    def set_data_encerramento(self, data_encerramento):
        self._data_encerramento = data_encerramento

    def get_data_encerramento(self):
        return self._data_encerramento

    def set_data_inicio_sintomas(self, data_encerramento):
        self._data_inicio_sintomas = data_inicio_sintomas

    def get_data_inicio_sintomas(self):
        return self._data_inicio_sintomas

    def set_sintomas(self, sintomas):
        self._sintomas = sintomas

    def get_sintomas(self):
        return self._sintomas

    def set_classificacao(self, classificacao):
        self._classificacao = classificacao

    def get_classificacao(self):
        return self._classificacao

    def set_estado_teste(self, estado_teste):
        self._estado_teste = estado_teste

    def get_estado_teste(self):
        return self._estado_teste

    def set_condicoes(self, condicoes):
        self._condicoes = condicoes

    def get_condicoes(self):
        return self._condicoes

    def set_descr_sintomas_outros(self, descr_sintomas_outros):
        self._descr_sintomas_outros = descr_sintomas_outros

    def get_descr_sintomas_outros(self):
        return self._descr_sintomas_outros

    def set_paciente(self, paciente):
        self._paciente = paciente

    def get_paciente(self):
        return self._paciente

    def set_evolucao(self, evolucao):
        self._evolucao = evolucao

    def get_evolucao(self):
        return self._evolucao

    def set_resultado(self, resultado):
        self._resultado = resultado

    def get_resultado(self):
        return self._resultado
