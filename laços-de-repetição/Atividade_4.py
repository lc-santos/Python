'''04) - Faça um algoritmo que receba “N” números e mostre positivo, negativo ou zero para cada número.'''

loop = True

while loop == True:
    n = float(input("Digite um número: "))
    if n < 0:
        print("Número negativo")
    if n == 0:
        print("Zero")
    if n > 0:
        print("Número positivo")
    new = int(input("Deseja consultar novamente?: [1] Sim [2] Não "))
    if new == 1:
        continue
    if new == 2:
        print("Fim do programa")
        break