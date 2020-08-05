'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado

Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;


'''


class Quadrado():
    tamanhoDoLado = 0
    
    def setLado(self, novoValor):
        self.tamanhoDoLado = novoValor
    
    def getLado(self):
        return self.tamanhoDoLado
    
    def calcularArea(self):
        return (self.tamanhoDoLado ** 2)
 
#Exemplo de uso
quadrado = Quadrado()
quadrado.setLado(5)
print(quadrado.getLado())
print(quadrado.calcularArea())