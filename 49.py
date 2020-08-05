'''
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material

Métodos: trocaCor e mostraCor

'''

class Bola():
    cor = ''
    circunferencia = 0
    material = ''
 
    def trocaCor(self, novaCor):
        self.cor = novaCor
    
    def mostraCor(self):
        print(self.cor)
 
#Exemplo de funcionamento:
bola = Bola()
bola.trocaCor('Amarela')
bola.mostraCor()