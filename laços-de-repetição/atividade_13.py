'''13) - Desenvolva um algoritmo que receba um valor como limite inicial e outro valor como limite final.
      Ao final exibir quantos valores no intervalo informados são pares e ímpares.'''

valorinicial = int(input("Qual o valor inicial?: "))
valorfinal = int(input("Qual o valor final?: "))
pares = 0
impares = 0

# Resolver resultado par

while valorinicial > -1:
    if valorinicial % 2 == 0:
        pares = pares + 1
        print(f'{valorinicial} é par')
        valorinicial = valorinicial + 1
        print(f'{valorinicial} é impar')
        impares = impares + 1
        valorinicial = valorinicial + 1
        if valorinicial >= valorfinal:
            print(f'Total de números pares {pares}')
            print(f'Total de números impares: {impares}')
            break

    if valorinicial % 2 == 1:
        impares = impares + 1
        print(f'{valorinicial} é impar')
        valorinicial = valorinicial + 1
        pares = pares + 1
        if valorinicial >= valorfinal:
            print(f'Total de números pares {pares}')
            print(f'Total de números impares: {impares}')
            break

