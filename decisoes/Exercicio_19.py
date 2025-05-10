''' 19.	Desenvolva um algoritmo que leia três valores inteiro informado pelo usuário e ao final exiba o maior valor entre eles.'''

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))

if n1 > n2:
    if n1 > n3:
        print(f'{n1} É o maior número')
        
if n2 > n1:
    if n2 > n3:
        print(f'{n2} É o maior número')

if n3 > n1:
    if n3 > n2:
        print(f'{n3} É o maior número')
