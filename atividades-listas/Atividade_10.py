'''10) - Desenvolva um programa em python que leia 10 valores inteiros informado pelo usuário. No final exibir o menor valor cadastrado no vetor.'''

lista = []

for i in range(1,11,1):
    num = int(input(f"Informe o {i}° valor: "))
    lista.append(num)

print(f"O menor valor da lista é {min(lista)}")