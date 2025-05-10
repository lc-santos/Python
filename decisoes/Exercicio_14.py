'''14.	Escreva um algoritmo que leia 3 valores inteiros (considere que não serão informados valores iguais) e escrever o maior deles.'''

n1 = int(input("Qual o primeiro valor?: "))
n2 = int(input("Qual o segundo valor?: "))
n3 = int(input("Qual o terceiro valor?: "))

if n1 >= n2:
    if n2 >= n3:
        print(f'{n1} é o maior número')

if n2 >= n1:
    if n2 >= n3:
        print(f'{n2} é o maior número')
        
if n3 >= n1:
    if n3 >= n2:
        print(f'{n3} é o maior número')