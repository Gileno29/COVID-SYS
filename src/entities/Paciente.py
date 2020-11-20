__author___ = "Gileno Cordeiro Duarte"

from Endereco import Endereco


class Paciente:

    def __init__(self):
        self._source_id = ''
        self._idade = ''
        self._sexo = ''
        self._sintomas = []
        self._municipio = ''
        self._estado = ''
        self._endereco = Endereco()

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

    def set_endereco(self, endereco):
        self._endereco = endereco

    def get_endereco(self):
        return self._endereco