__author___ = "Gileno Cordeiro Duarte"


class Paciente:

    def __init__(self):
        self._source_id = ''
        self._idade = ''
        self._sexo = ''
        self._sintomas = {}
        self._endereco = {}
        self._teste = {}

    def set_source_id(self, source_id):
        self._source_id = source_id

    def get_source_id(self):
        return self._source_id

    def set_idade(self, idade):
        self._idade = idade

    def get_idade(self):
        return self._idade

    def set_sintomas(self, sintomas):
        self._sintomas = sintomas

    def get_sintomas(self):
        return self._sintomas

    def set_endereco(self, endereco):
        self._endereco = endereco

    def get_endereco(self):
        return self._endereco

    def set_sexo(self, sexo):
        self._sexo = sexo

    def get_sexo(self):
        return self._sexo

    def set_resultado_teste(self, resultado):
        self._resultado = resultado

    def get_resultado_teste(self):
        return self._resultado
