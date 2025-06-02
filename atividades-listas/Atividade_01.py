'''1) - Desenvolva um programa em python que receba 10 valores informados pelo usuário, armazene-os em um vetor, exiba os dados do vetor'''
import random

valores = []

for cont in range(1,11,1):
    # valor = int(input(f'Informe o {cont} valor: '))
    #valores.append(valor)
    #valores.append(int(input(f'Informe o {cont} valor: ')))
    valores.append(int(input(f"informe o {cont} valor: ")))
print(type(valores))
print(valores)