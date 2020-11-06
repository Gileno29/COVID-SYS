__author___ = "Gileno Cordeiro Duarte"


class Paciente:

    def __init__(self):
        self._source_id = ''
        self._idade = ''
        self._sintomas = []
        self._municipio = ''
        self._estado = ''

    def set_source_id(self, nome):
        self._nome = nome

    def get_source_id(self):
        return self._nome

    def set_idade(self, idade):
        self._idade = idade

    def get_idade(self):
        return self._idade

    def set_sintomas(self, sintomas):
        self._sintomas.append(sintomas)

    def get_sintomas(self):
        return self._sintomas

    def set_municipio(self, municipio):
        self._municipio = municipio

    def get_municipio(self):
        return self._municipio

    def set_estado(self, estado):
        self._estado = estado

    def get_estado(self):
        return self._estado
