class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []
    def abrindo_contas(self,conta):
        self.contas.append(self)
        for c in self.contas:
            c.resumo()