# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

# comprar apenas latas de 18 litros;

# comprar apenas galões de 3,6 litros;

# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

# Obs: Sem utilizar tomada de decisão, nem eu consegui fazer essa questão (devido a no último item ser solicitado a combinação que resulta no menor preço). Entretanto, tentem fazer algo o mais parecido o possível com o que a questão pede!

import math
metrosQuadrados = float(input('Digite os m²: '))
metrosQuadradosMaisDez = metrosQuadrados * 1.0
 
rendimentoLitro = 6
litrosLata = 18
precoLata = 80
rendimentoLata = rendimentoLitro * litrosLata
litrosGalao = 3.6
precoGalao = 25
rendimentoGalao = rendimentoLitro * litrosGalao
 
somenteLatas = math.ceil(metrosQuadrados / rendimentoLata)
somenteGaloes = math.ceil(metrosQuadrados / rendimentoGalao)
latas = math.floor(metrosQuadradosMaisDez / rendimentoLata)
galoes = math.ceil((metrosQuadradosMaisDez % rendimentoLata) / rendimentoGalao)
 
print(
    f'Somente Latas: {somenteLatas}, custando R${somenteLatas * precoLata}\n'
    f'Somente Galões: {somenteGaloes}, custando R${somenteGaloes * precoGalao}\n'
    f'Latas: {latas} , Galões: {galoes}, '
    f'custando R${((latas * precoLata) + (galoes *precoGalao)):.2f}')

    