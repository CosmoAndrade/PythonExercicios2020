'''
Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.

'''

class ContaInvestimento():
    def __init__(self, numero, nome, saldo = 0, taxaJuros = 0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        self.__taxaJuros = taxaJuros/100 #O valor será passado em percentual
    
    def alterarNome(self, novoNome):
        self.nome = novoNome
    def deposito(self, valor):
        self.saldo += valor
    def saque(self, valor):
        self.saldo -= valor
    def adicioneJuros(self):
        self.saldo *= (1+self.__taxaJuros)
 
conta = ContaInvestimento(1, 'Joao', 1000, 10)
print(f'Saldo: R${conta.saldo:.2f}') #Saldo: R$1000.00
conta.adicioneJuros()
conta.adicioneJuros()
conta.adicioneJuros()
conta.adicioneJuros()
conta.adicioneJuros()
print(f'Saldo: R${conta.saldo:.2f}') #Saldo: R$1610.51