'''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:

tipoCombustivel.

valorLitro

quantidadeCombustivel

Possua no mínimo esses métodos:

abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo

abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.

alterarValor( ) – altera o valor do litro do combustível.

alterarCombustivel( ) – altera o tipo do combustível.

alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

'''

class BombaDeCombustivel():
    def __init__(self, pGasolina, pAlcool, gasolina = 0, alcool = 0, tipo = "g"):
        self.pGasolina = pGasolina # Preço do litro de Gasolina
        self.pAlcool = pAlcool
        # Testa se o tipo de combustivel é dos dois um: Álcool ou Gasolina.
        # Se não for, coloca gasolina como padrão
        if (tipo == "g" or tipo == "a"):
            self.tipo = tipo
        else:
            self.tipo = "g"
        self.gasolina = gasolina # Quantidade de Gasolina na bomba
        self.alcool = alcool
 
    def abastecerPorValor(self, valor):
        if self.tipo == "g":
            self.auxLitros = valor / self.pGasolina
            if self.auxLitros <= self.gasolina:
                self.gasolina -= self.auxLitros
                print(f"{self.auxLitros:.2f} Litros de gasolina abastecidos por R${valor:.2f}")
            else:
                print(f"Não tem tanto combustível na bomba")
 
        elif self.tipo == "a":
            self.auxLitros = valor / self.pAlcool
            if self.auxLitros <= self.alcool:
                self.alcool -= self.auxLitros
                print(f"{self.auxLitros:.2f} Litros de alcool abastecidos por R${valor:.2f}")
            else:
                print(f"Não tem tanto combustível na bomba")
    
    def abastecerPorLitro(self, litros):
        if self.tipo == "g":
            if litros <= self.gasolina:
                self.gasolina -= litros
                print(f"{litros:.2f} Litros de gasolina abastecidos por R${litros*self.pGasolina:.2f}")
            else:
                print(f"Não tem tanto combustível na bomba")
 
        elif self.tipo == "a":
            if litros <= self.alcool:
                self.alcool -= litros
                print(f"{litros:.2f} Litros de alcool abastecidos por R${litros*self.pAlcool:.2f}")
            else:
                print(f"Não tem tanto combustível na bomba")
 
    def alterarValor(self, novoValor):
        if self.tipo == "g":
            self.pGasolina = novoValor
        elif self.tipo == "a":
            self.pAlcool = novoValor
 
    def alterarCombustivel(self, novoCombustivel):
        if novoCombustivel.lower() == "g":
            self.tipo = "g"
        elif novoCombustivel.lower() == "a":
            self.tipo = "a"
 
    def alterarQuantidadeCombustivel(self, novaQuantidade):
        if self.tipo == "g":
            self.gasolina = novaQuantidade
        elif self.tipo == "a":
            self.alcool = novaQuantidade
# Teste: 
bomba = BombaDeCombustivel(5, 4, 1000, 1000)
bomba.abastecerPorValor(45)
bomba.alterarValor(6)
bomba.abastecerPorLitro(9)
bomba.alterarCombustivel('a')
bomba.abastecerPorLitro(9000)
bomba.alterarQuantidadeCombustivel(12000)
bomba.abastecerPorLitro(9000)