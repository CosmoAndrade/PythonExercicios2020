'''
Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário. Dica: acrescente um método especial str() à classe Bichinho.

'''

class Tamagushi():
    def __init__(self, nome):
        self.__nome = nome
        self.__fome = 0 
        self.__saude = 0
        self.__idade = 0
        
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
        return f'nome : {self.nome}\nfome : {self.fome}\nsaude : {self.saude}\nidade : {self.idade}\nhumor : {self.humor}'
 
#exemplo de uso
tamagushi = Tamagushi('Tama')
tamagushi.fome = 30
tamagushi.saude = 80
tamagushi.idade = 20
print(tamagushi)
 
tamagushi.alimentar = 'banana'
tamagushi.alimentar = 'maçã'
tamagushi.brincar = 10
print(tamagushi)
 
 
# saída
# nome : Tama
# fome : 30
# saude : 80
# idade : 20
# humor : 75.0
# nome : Tama
# fome : 17
# saude : 90
# idade : 20
# humor : 86.5
Visão geral
Perguntas e respostas