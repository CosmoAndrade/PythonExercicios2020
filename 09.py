# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.

# - C = (5 * (F-32) / 9).

grausFarenheit = float(input('Digite a temperatura em Farenheit: '))
grausCelsius = (5 * (grausFarenheit - 32) / 9)
print(f'{grausFarenheit:.2f} graus Farenheit correspondem a {grausCelsius:.2f} graus Celsius')