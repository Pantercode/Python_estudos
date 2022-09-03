from clientes_banco import Cliente
from contas_banco import Conta,ContaEspecial
from lista_unica_banco import *
marcell = Cliente('Marcell Felipe de Paula Oliveira','98888-7611')
emilly = Cliente('Emilly de Araújo de Oliveira ','98150-7000')
fabiana = Cliente('Fabiana Figueiredo de Araújo de Oliveira','98150-7000')

conta1 = Conta([marcell,emilly],100)
conta2 = ContaEspecial([emilly,marcell], 2, 500, 1000)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()
lis = ListaUnica(int)
lis.adiciona(5)
lis.adiciona(3)
lis.adiciona(2.5)