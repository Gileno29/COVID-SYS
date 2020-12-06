__author___ = "Gileno Cordeiro Duarte"


class Endereco:

    def __init__(self):
        self._pais = ''
        self._estado = ''
        self._municipio = ''

    def set_pais(self, bairro):
        self._bairro = bairro

    def get_pais(self):
        return self._bairro

    def set_estado(self, estado):
        self._estado = estado

    def get_estado(self):
        return self._estado

    def set_municipio(self, municipio):
        self._municipio = municipio

    def get_municipio(self):
        return self._municipio
