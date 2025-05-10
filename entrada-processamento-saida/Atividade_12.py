#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

hora = float(input("Quanto recebe por hora?: "))
horas_mes = int(input("Quantas horas trabalhadas no mês?: "))

salario = hora * horas_mes

print ("Seu salário será de: R$",salario)

