# 13. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) O produto do dobro do primeiro com metade do segundo.
# b) A soma do triplo do primeiro com o terceiro.

n1 = int(input("Informe o primeiro número inteiro: "))
n2 = int(input("Informe o segundo número inteiro: "))
n3 = float(input("Infome um terceiro número real: "))


print ("O produto do dobro de {} que é {} somado a metade de {} que é {:.0f}, resulta em {:.0f}".format(n1,n1*2,n2,n2/2,(n1*2) + (n2/2)))
print("A soma do triplo de {} que é {} somado a {}, resulta em {}".format(n1,n1*3,n3,(n1*3) + n3))