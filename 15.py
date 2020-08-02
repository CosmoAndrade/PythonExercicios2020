# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# 1 - salário bruto.

# 2 - quanto pagou ao INSS.

# 3 - quanto pagou ao sindicato.

# 4 - o salário líquido.

# calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
#   Obs.: Salário Bruto - Descontos = Salário Líquido. 

precoHora = float(input('Digite quanto você ganha por hora: '))
horasTrabalhadas = float(input('Digite quantas horas você trabalhou esse mês: '))
salarioBruto = precoHora * horasTrabalhadas
IR = salarioBruto * (11/100)
INSS = salarioBruto * (8/100)
sindicato = salarioBruto * (5/100)
salarioLiquido = salarioBruto - IR - INSS - sindicato
print(f'+ Salário Bruto : R${salarioBruto:.2f}')
print(f'- IR (11%) : R${IR:.2f}')
print(f'- INSS (8%) : R${INSS:.2f}')
print(f'- Sindicato (5%) : R${sindicato:.2f}')
print(f'= Salário Liquido : R${salarioLiquido:.2f}')



