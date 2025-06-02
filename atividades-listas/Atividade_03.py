'''3) Desenvolva um programa em python que receba 15 valores informados pelo usuário armazene-os em vetor chamando num, e imprima uma listagem numerada contendo a seguinte mensagem "par" ou "impar"
de acordo com os valores cadastrados no vetor'''
from random import randint

num = []

for cont in range(1,16,1):
    num.append(int(input(f'informe o {cont} valor: ')))
    #num.append(randint(10,99))
for numero in num:
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
    