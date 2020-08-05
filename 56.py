'''
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.

'''


class Macaco():
    def __init__(self, nome):
        self.__nome = nome
        self.__bucho = []
 
    def comer(self, alimento):
        if type(alimento) == str:
            self.__bucho.insert(0,alimento)
            #adiciona o alimento no começo da lista bucho
    
    def verBucho(self):
        #o laço for vai percorrer cada item da lista bucho
        #cada iteração do laço, o item atual de bucho vai ser
        #representado pelo nome "comida"
        for comida in self.__bucho:
            print(f'macaco: {self.__nome} comida: {comida}')
    
    def digerir(self):
        #esvaziamos o bucho
        self.__bucho = []
 
macaco1 = Macaco('João')
macaco2 = Macaco('Maria')
macaco1.verBucho()
macaco2.verBucho()
macaco1.comer('Banana')
macaco2.comer('Banana')
print() #apenas para quebra de linha da saída
macaco1.verBucho()
macaco2.verBucho()
macaco1.comer('Maçã')
macaco2.comer('Uva')
print() #apenas para quebra de linha da saída
macaco1.verBucho()
macaco2.verBucho()
macaco1.digerir() #Só o primeiro macaco digeriu a comida
macaco1.comer('Melão')
macaco2.comer('Banana')
print() #apenas para quebra de linha da saída
macaco1.verBucho()
macaco2.verBucho()
 
#saída (primeira linha em branco pois o bucho de ambos estava vazio)
#
# macaco: João comida: Banana
# macaco: Maria comida: Banana
#
# macaco: João comida: Maçã
# macaco: João comida: Banana
# macaco: Maria comida: Uva
# macaco: Maria comida: Banana
#
# macaco: João comida: Melão
# macaco: Maria comida: Banana
# macaco: Maria comida: Uva
# macaco: Maria comida: Banana