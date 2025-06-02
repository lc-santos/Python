'''8) - Desenvolva um programa em python que receba 10 valores numéricos e guarde-os em uma lista. Verifique se os valores cadastrados são pares ou 
ímpares e cadastre os valores pares em uma nova lista e os ímpares em outra lista. No final exibir o conteúdo das três listas.'''

lista = []
listapar = []
listaimpar = []


for i in range(1,11,1):
    num = int(input(f"Informe o {i}° valor: "))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
        
print(f"Lista dos valores ímpares: {listaimpar}")
print(f"Lista dos valores pares: {listapar}")
print(f"Lista dos valores informados: {lista}")
