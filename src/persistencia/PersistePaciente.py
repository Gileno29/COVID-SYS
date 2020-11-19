from persistencia.conexao import ConexaoBD


class PersistePaciente:

    def __init__(self, paciente):
        pass

    def savePaciente(self, paciente):
        conexao = ConexaoBD.conexao()
        self.con = conexao.conectar()
