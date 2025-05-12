valorinicial = int(input("Qual o valor inicial?: "))
valorfinal = int(input("Qual o valor final?: "))
pares = 0
impares = 0

while valorinicial > 0:
    if valorinicial % 2 == 0:
        print(f'{valorinicial} é par')
        pares = pares + 1
        valorinicial = valorinicial + 1
        print(f'{valorinicial} é impar')
        impares = impares + 1
        valorinicial = valorinicial + 1
        if valorinicial >= valorfinal:
            print(f'Total de números pares {pares}')
            print(f'Total de números impares: {impares}')
            break
    if valorinicial % 2 ==1:
        print(f'{valorinicial} é impar')
        impares = impares + 1
        valorinicial = valorinicial + 2
        if valorinicial >= valorfinal:
            print(f'Total de números pares {pares}')
            print(f'Total de números impáres: {impares}')
            break

