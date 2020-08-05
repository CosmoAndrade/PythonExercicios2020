'''

Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.

Possua uma classe chamada Retangulo, com os atributos largura e altura.

Possua uma função para imprimir os valores da classe Ponto

Possua uma função para encontrar o centro de um Retângulo.

Você deve criar alguns objetos da classe Retangulo.

Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.

A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.

O valor do centro do objeto deve ser mostrado na tela

Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

'''

class Ponto():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
 
class Retangulo(): 
    def __init__(self, partida, largura = 0, altura = 0):
        self.__largura = largura
        self.__altura = altura
        self.__xVertice = partida.x
        self.__yVertice = partida.y
        
    #Temos que definir o property mesmo que não o usemos
    #Para que o setter funcione
    @property
    def xVertice(self):
        return self.__xVertice
    @xVertice.setter
    def xVertice(self, novoValor):
        self.__xVertice = novoValor
    
    @property
    def yVertice(self):
        return self.__yVertice
    @yVertice.setter
    def yVertice(self, novoValor):
        self.__yVertice = novoValor
 
    @property
    def centro(self):
        self.__xCentro = self.__xVertice + (self.__largura/2)
        self.__yCentro = self.__yVertice + (self.__altura/2)
        self.__pontoCentro = Ponto(self.__xCentro ,self.__yCentro)
        return self.__pontoCentro
 
#Exemplo de uso
ponto = Ponto(1,2)
retangulo = Retangulo(ponto, 10, 20)
while True: #Menu
    print(f'X do centro: {retangulo.centro.x}\nY do centro: {retangulo.centro.y}')
    retangulo.xVertice = float(input('\nDigite o novo x do vértice: '))
    retangulo.yVertice = float(input('Digite o novo y do vértice: '))