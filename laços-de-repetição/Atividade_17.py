'''17) - Desenvolva um algoritmo que leia 10 valores e ao final exiba a quantidade de valores múltiplo de 5.'''


divs = 0

for i in range(1,11,1):
    valor = int(input(f"informe o {i} valor: "))
    if valor % 5 == 0:
        divs = divs + 1

print(f"Total de números múltiplo de 5: {divs}")
