__author___ = "Gileno Cordeiro Duarte"


class Paciente:

    def __init__(self):
        self._paciente_cbo = ''
        self._paciente_idade = ''
        self._paciente_sexo = ''
        self._paciente_endereco = ''
        self._paciente_profissional_de_saude = ''
        self._paciente_profissional_de_seguranca = ''
        self._dados_teste = {}

    def set_paciente_cbo(self, paciente_cbo):
        self._paciente_cbo = paciente_cbo

    def get_paciente_cbo(self):
        return self._paciente_cbo

    def set_paciente_idade(self, paciente_idade):
        self._paciente_idade = paciente_idade

    def get_paciente_idade(self):
        return self._paciente_idade

    def set_paciente_endereco(self, paciente_endereco):
        self._paciente_endereco = paciente_endereco

    def get_paciente_endereco(self):
        return self._paciente_endereco

    def set_paciente_sexo(self, paciente_sexo):
        self._paciente_sexo = paciente_sexo

    def get_paciente_sexo(self):
        return self._paciente_sexo

    def set_paciente_profissional_de_saude(self, paciente_profissional_de_saude):
        self._paciente_profissional_de_saude = paciente_profissional_de_saude

    def get_paciente_profissional_de_saude(self):
        return self._paciente_profissional_de_saude

    def set_paciente_profissional_de_seguranca(self, paciente_profissional_de_seguranca):
        self._paciente_profissional_de_seguranca = paciente_profissional_de_seguranca

    def get_paciente_profissional_de_seguranca(self):
        return self._paciente_profissional_de_seguranca

    def set_dados_teste(self, dados_teste):
        self._dados_teste = dados_teste

    def get_dados_teste(self):
        return self._dados_teste
