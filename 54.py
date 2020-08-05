'''
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

'''

class Televisor():
    def __init__(self, volume = 20, canal = 10):
        self.__volume = volume
        self.__canal = canal
    
    #Uma forma de criar um setter sem escrever algo do tipo
    #setVolume() é utilizar o property
    #o que ele faz é possibilitar que usemos um getter ou setter
    #chamando apenas o nome da variável que queremos utilizar
    @property 
    def volume(self):
        return self.__volume
    #O que isso faz é chamar a função acima como se fosse uma
    #variável, utilizando acessando assim: objeto.volume
    #Obviamente que nesse caso não faz diferença nenhuma
    #pois tudo que isso faz é retornar o volume sem realizar
    #nenhum tratamento do dado
 
    #Já para o setter, utilizamos a sintaxe abaixo
    @volume.setter
    def volume(self, novoVolume):
        #Se o novo volume for um inteiro entre 0 e 100
        if type(novoVolume) == int and novoVolume >= 0 and novoVolume <= 100:
            self.__volume = novoVolume
    #Aqui já podemos ver uma utilidade maior, visto que 
    #há um teste antes de setarmos o valor do atributo
    #Chamamos o método escrevendo apenas objeto.volume = 3
    #ao invés de chamar algo como objeto.setVolume(3)
    #onde 3 é um volume qualquer
    #O bom disso é que não precisamos lembrar de dois nomes
    #(setVolume e getVolume)
    #isso deixa a usabilidade melhor
 
    @property
    def canal(self):
        return self.__canal
 
    @canal.setter
    def canal(self, novoCanal):
        #Como não sei os parâmetros que definem os canais de TV
        #vou apenas testar se recebemos um número inteiro
        if type(novoCanal) == int:
            self.__canal = novoCanal
 
#exemplo de uso
tv1 = Televisor()
print(f'canal: {tv1.canal}')
print(f'volume: {tv1.volume}')
tv1.canal = 11
tv1.volume = 45
print(f'novo canal: {tv1.canal}')
print(f'novo volume: {tv1.volume}')
 
#saída
#>canal: 10
#>volume: 20
#>novo canal: 11
#>novo volume: 45