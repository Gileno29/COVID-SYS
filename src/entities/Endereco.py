__author___ = "Gileno Cordeiro Duarte"


class Endereco:

    def __init__(self):
        self._rua = ''
        self._bairro = ''
        self._estado = ''
        self._municipio = ''

    def set_rua(self, rua):
        self._rua = rua

    def get_rua(self):
        return self._rua

    def set_bairo(self, bairro):
        self._bairro = bairro

    def get_bairro(self):
        return self._bairro

    def set_estado(self, estado):
        self._estado = estado

    def get_estado(self):
        return self._estado

    def set_municipio(self, municipio):
        self._municipio = municipio

    def get_municipio(self):
        return self._municipio
