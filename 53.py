'''
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.


'''

class ContaCorrente():
    def __init__(self, numero, nome, saldo = 0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
    
    def alterarNome(self, novoNome):
        self.nome = novoNome
    def deposito(self, valor):
        self.saldo += valor
    def saque(self, valor):
        self.saldo -= valor
 
#Exemplo de uso
conta1 = ContaCorrente('001', 'Rodolfo')
print(conta1.saldo)
conta1.deposito(500)
print(conta1.saldo)
conta1.saque(300)