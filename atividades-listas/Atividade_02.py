'''2) Desenvolva um programa em python que receba 10 nomes informados pelo usuário e armazene-os em um vetor chamado nomes. No final exiba uma lista numerada com os nomes
cadastrados no vetor'''

nomes= []

for cont in range(1, 11, 1):
    nomes.append(input(f'informe o {cont} primeiro nome: ')
                )
# imprimir uma lista numerada

#i = 1
#while i <= 10:
#    print(f'{i}° - {nomes[i-1]}')
#    i += 1

i = 1
for nome in nomes:
    print(f'{i}° - {nome}')
    i += 1

