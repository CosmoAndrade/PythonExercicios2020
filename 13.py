# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

# 1 - Para homens: (72.7*h) - 58

# 2 - Para mulheres: (62.1*h) - 44.7

 altura = float(input('Digite sua altura em metros: '))
pesoIdealHomem = (72.7 * altura) - 58
pesoIdealMulher = (62.1 * altura) - 44.7
print(f'O peso ideal para sua altura é:\n{pesoIdealHomem:.2f}Kg para homens.\n{pesoIdealMulher:.2f}Kg para mulheres.')



