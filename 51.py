'''

Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)

Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

'''

class Retangulo():
    comprimento = 0
    largura = 0
 
    def setComprimento(self, novoValor):
        self.comprimento = novoValor
    def setLargura(self, novoValor):
        self.largura = novoValor
    def getComprimento(self):
        return self.comprimento
    def getLargura(self):
        return self.largura
    def calcularArea(self):
        return (self.largura * self.comprimento)
    def calcularPerimetro(self):
        return (self.largura * 2 + self.comprimento * 2)
 
comprimento = float(input("Digite o comprimento do local: "))
largura = float(input("Digite a largura do local: "))
retangulo = Retangulo()
retangulo.setComprimento(comprimento)
retangulo.setLargura(largura)
print(f"Você vai precisar de {retangulo.calcularArea()}m² de piso")
print(f"Você vai precisar de {retangulo.calcularPerimetro()}m de rodapés")