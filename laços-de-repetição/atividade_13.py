'''13) - Desenvolva um algoritmo que receba um valor como limite inicial e outro valor como limite final.
      Ao final exibir quantos valores no intervalo informados são pares e ímpares.'''

valorinicial = int(input("Qual o valor inicial?: "))
valorfinal = int(input("Qual o valor final?: "))
par = 0
impar = 0
loop = valorfinal

for i in range (valorinicial,valorfinal + 1,1):
    if i % 2 == 0:
        print(f'{i} é par')
        par = par + 1
        print(f'total de par {par}')
    if i % 2 != 0:
        print(f'{i} é impar')
        impar = impar + 1
        print(f'total de impar {impar}')