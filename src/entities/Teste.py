class Teste:

    def __init__(self):

        self._data_teste = ''
        self._data_notificacao = ''
        self._resultado = ''

    def set_data_teste(self, data):
        self._data_teste = data

    def get_data_teste(self):
        return self._data_teste

    def set_data_notificacao(self, data):
        self._data_notificacao = data

    def get_data_notificacao(self):
        return self._data_notificacao

    def set_resultado(self, resultado):
        self._resultado = resultado

    def get_resultado(self):
        return self._resultado
