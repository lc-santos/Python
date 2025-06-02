'''6) - Desenvolva um programa em python que leia valores inteiros e armazene-os em um vetor, calcule e exiba as seguinte informações:
   a) - A quantidade de números pares.
   b) - Os números pares.
   c) - A quantidade de números ímpares.
   d) - Os valores ímpares.
   e) - A média dos valores pares.
   f) - A média dos valores ímpares.
   g) - A média da soma dos valores pares mais os valores ímpares.'''
   
lista = []
pares = []
impar = []
 

for i in range(1,11,1):

    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares.append(num)
    else: impar.append(num)

print(f"Números impar: {impar}")
print(f"Quantidade de números impar: {len(impar)}")
print(f"Números par: {pares}")
print(f"Quantidades de números par {len(pares)}")
print(f"A média dos valores ímpares {sum(impar) / len(impar)}")
print(f"A média dos valores pares {sum(pares) / len(pares)}")
print(f"A média da soma dos valores pares mais ou valores ímpares {sum(impar + pares) / len(impar + pares)}")
