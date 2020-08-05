'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura

Métodos: Envelhecer, engordar, emagrecer, crescer.

Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

'''

class Pessoa():
    nome = ''
    idade = 0.0
    peso = 0.0
    altura = 0.0
 
    def envelhecer(self, anos):
        #Se a idade for menor que 21 precisa crescer também
        if self.idade < 21:                 
            #Se envelheceu até 21 anos ou menos
            if (anos + self.idade) <= 21:   
                #Cresce 0,5 cm por ano envelhecido
                self.crescer(anos * 0.5)    
            #Se envelheceu até mais de 21 anos
            else:                           
                #Só cresceu até os 21
                self.crescer((21 - self.idade) * 0.5)
        self.idade += anos
 
    def engordar(self, quilos):
        self.peso += quilos
 
    def emagrecer(self, quilos):
        self.peso -= quilos
 
    def crescer(self, cm):
        self.altura += cm