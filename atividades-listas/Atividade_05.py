'''5) - Desenvolva um programa em python que leia 30 valores inteiros e armazene-os em um vetor. Exiba os valores do vetor
ao contrário da ordem de leitura dos valores.'''

lista = []

for i in range(1,31,1):
    lista.append(int(input("Digite um número: ")))
    print(lista[::-1])