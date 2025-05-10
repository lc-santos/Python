'''18.	Escreva um algoritmo que leia dois valores inteiros e imprimir uma das três mensagens a seguir:
‘Números iguais’, caso os números sejam iguais
‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
‘Segundo maior’, caso o segundo seja maior que o primeiro.'''

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

if n1 > n2:
    print("Primeiro é maior")
else:
    if n2 > n1:
        print("Segundo é maior")
    else:
        if n1 == n2:
            print("Números iguais")