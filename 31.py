'''
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

'''

diaInt = int(input('Digite o número do dia da semana: '))
diaStr = ''
if diaInt == 1:
    diaStr = 'Domingo'
elif diaInt == 2:
    diaStr = 'Segunda'
elif diaInt == 3:
    diaStr = 'Terça'
elif diaInt == 4:
    diaStr = 'Quarta'
elif diaInt == 5:
    diaStr = 'Quinta'
elif diaInt == 6:
    diaStr = 'Sexta'
elif diaInt == 7:
    diaStr = 'Sábado'
 
if diaStr == '':
    print('Valor inválido')
else:
    print(f'O dia correspondente é {diaStr}')
