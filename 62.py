'''
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.

Exemplo de uso:

harry = funcionário("Harry",25000)
harry.aumentarSalario(10)


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
    def aumentarSalario(self, percentual):
        self.salario *= 1 + (percentual/100)
        
funcionario = Funcionario('Joao', 1000)
print(funcionario.getNome()) #Joao
print(funcionario.getSalario()) #1000.0
 
harry = Funcionario("Harry",25000)
print(harry.getNome()) #Harry
print(harry.getSalario()) #25000.0
harry.aumentarSalario(10)
print(harry.getNome()) #Harry
print(harry.getSalario()) #27500.0