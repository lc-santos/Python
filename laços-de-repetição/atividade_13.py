'''13) - Desenvolva um algoritmo que receba um valor como limite inicial e outro valor como limite final.
      Ao final exibir quantos valores no intervalo informados são pares e ímpares.'''

valorinicial = int(input("Qual o valor inicial?: "))
valorfinal = int(input("Qual o valor final?: "))
par = 0
impar = 0
loop = valorfinal

while valorfinal > 0:
    if valorinicial % 2 == 0:
        print(f"{valorfinal} impar")
        valorifinal = valorfinal - 1
        print(f"{valorfinal} par")   
    else:
        print(f"{valorfinal} par")
        valorfinal = valorfinal - 1
        print(f"{valorfinal} impar")