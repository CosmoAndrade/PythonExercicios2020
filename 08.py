# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 

salarioHora = float(input('Digite quanto você ganha por hora: '))
horasTrabalhadasMes = float(input('Digite quantas horas você trabalhou esse mês: '))
salarioTotal = salarioHora * horasTrabalhadasMes
print(f'Ganhando R${salarioHora:.2f} a hora, tendo trabalhado {horasTrabalhadasMes} horas no mês, seu salário este mês é de R${salarioTotal:.2f}.')