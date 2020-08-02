# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit. 

grausCelsius = float(input('Digite a temperatura em Celsius: '))
grausFarenheit = ((grausCelsius * 9) / 5) + 32
print(f'{grausCelsius:.2f} graus Celsius correspondem a {grausFarenheit:.2f} graus Farenheit')