'''
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade

Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade

Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

'''

class Tamagushi():
    def __init__(self, nome):
        self.__nome = nome
        self.__fome = 0 
        #neste caso, um valor baixo em fome significa muita fome
        self.__saude = 0
        self.__idade = 0
    
    @property #property foi explicado na resolução do exercício 06
    def nome(self):
        return self.__nome
    @property 
    def fome(self):
        return self.__fome
    @property 
    def saude(self):
        return self.__saude
    @property 
    def idade(self):
        return self.__idade
 
    @nome.setter #também explicado na resolução do exercício 06
    def nome(self, novoNome):
        if type(novoNome) == str:
            self.__nome = novoNome
    @fome.setter 
    def fome(self, novaFome):
        if type(novaFome) == int:
            self.__fome = novaFome
    @saude.setter 
    def saude(self, novaSaude):
        if type(novaSaude) == int:
            self.__saude = novaSaude
    @idade.setter 
    def idade(self, novaIdade):
        if type(novaIdade) == int:
            self.__idade = novaIdade
    
    @property
    def humor(self):
        #vou simplesmente tirar a média aritmética
        #dos atributos fome e saúde
        return (self.__fome + self.__saude)/2
 
#exemplo de uso
tamagushi = Tamagushi('Tama')
print(f'nome : {tamagushi.nome}')
print(f'fome : {tamagushi.fome}')
print(f'saude : {tamagushi.saude}')
print(f'idade : {tamagushi.idade}')
print(f'humor : {tamagushi.humor}')
tamagushi.nome = 'Gushi'
tamagushi.fome = 100
tamagushi.saude = 80
tamagushi.idade = 20
print(f'novo nome : {tamagushi.nome}')
print(f'nova fome : {tamagushi.fome}')
print(f'nova saude : {tamagushi.saude}')
print(f'nova idade : {tamagushi.idade}')
print(f'novo humor : {tamagushi.humor}')
 
#saída
# nome : Tama
# fome : 0
# saude : 0
# idade : 0
# humor : 0.0
# novo nome : Gushi
# nova fome : 100
# nova saude : 80
# nova idade : 20
# novo humor : 90.0