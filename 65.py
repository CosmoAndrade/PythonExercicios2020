'''
Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigir que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.

'''

import random
class Tamagushi():
    def __init__(self, nome, fome = 0, saude = 0, idade = 0):
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade
        
    @property 
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
 
    @nome.setter 
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
    def alimentar(self):
        return ''
    @alimentar.setter
    def alimentar(self, alimento):
        if type(alimento) == str:
            alimento.lower()
            if alimento == 'banana':
                self.__fome -= 10
            elif alimento == 'castanha':
                self.__fome -= 5
            elif alimento == 'rosquinha':
                self.__fome -= 15
            else:
                self.__fome -= 3
            if self.__fome < 0:
                self.__fome = 0
    
    @property
    def brincar(self):
        return ''
    @brincar.setter
    def brincar(self, tempo):
        if type(tempo) == int:
            self.__saude += tempo
            if self.__saude > 100:
                self.__saude = 100
    
    @property
    def humor(self):
        return (100 - self.__fome + self.__saude)/2
 
    def __str__(self):
        return f'\nnome : {self.nome}\nfome : {self.fome}\nsaude : {self.saude}\nidade : {self.idade}\nhumor : {self.humor}'
 
 
fazenda = []
qtBichinhos = int(input('Digite quantos bichinhos você quer na fazenda: '))
for i in range(0, qtBichinhos):
    fazenda.insert(i,Tamagushi(input(f'Digite o nome do {i+1}º bichinho: ')))
    fazenda[i].fome = random.randint(0,100)
    fazenda[i].saude = random.randint(0,100)
    fazenda[i].idade = random.randint(0,100)
 
 
def exibirBichos():
    for bicho in fazenda:
        print(bicho)
 
def alimentarBichos():
    alimento = input('Digite o alimento a ser dado aos bichos: ').lower()
    for bicho in fazenda:
        bicho.alimentar = alimento
 
def brincarComBichos():
    tempo = int(input('Digite por quanto tempo vai brincar com os bichos: '))
    for bicho in fazenda:
        bicho.brincar = tempo
 
def menu():
    escolha = ''
    while escolha != 's':
        print('\nDigite:')
        print('A para alimentar os bichos.')
        print('B para brincar com os bichos.')
        print('E para exibir os dados dos bichos.')
        print('S para sair.')
        escolha = input('Sua escolha é: ').lower()
 
        if escolha == 'a':
            alimentarBichos()           
        elif escolha == 'b':
            brincarComBichos()
        elif escolha == 'e':
            exibirBichos()
        elif escolha == 's':
            pass
        else:
            print('\nEscolha inválida!\n')
 
menu()