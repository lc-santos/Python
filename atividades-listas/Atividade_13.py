'''13) - Desenvolva um programa em python que leia 15 valores informado pelo usuário e cadastre-os em uma lista. O usuário deverá informar um valor a ser procurado no vetor,
caso encontre este valor exiba o índice desse elemento.'''

lista = []

for i in range(1,16,1):
    num = int(input(f"Informe o {i} valor: "))
    lista.append(num)
    
valor = int(input("Qual valor deseja buscar na lista?: "))
if valor in lista:
    print(f"O valor {valor} está no índice {lista.index(valor)}")
else: print("Esse valor não esta na lista")