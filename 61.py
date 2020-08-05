'''
Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.


'''

class Funcionario():
    def __init__(self, nome, salario):
        if (type(nome) == str) and ((type(salario) == float) or (type(salario) == int)):
            self.nome = nome
            self.salario = float(salario)
    
    def getNome(self):
        return self.nome
    def getSalario(self):
        return self.salario
        
funcionario = Funcionario('Joao', 1000)
print(funcionario.getNome()) #Joao
print(funcionario.getSalario()) #1000.0