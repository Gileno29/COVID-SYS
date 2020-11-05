__author___ = "Gileno Cordeiro Duarte"


class Paciente:

    def __init__(self):
        self._id = ''
        self._idade = ''
        self._sintomas = []

    def set_nome(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_idade(self, idade):
        self._idade = idade

    def get_idade(self):
        return self._idade

    pass
