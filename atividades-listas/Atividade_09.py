'''9) - Desenvolva um programa em python que leia 10 valores numéricos informados pelo usuário e armazene-os em um vetor A, leia mais 10 valores numéricos informado pelo usuário 
armazene-os em outro vetor B, Gere um vetor C, que receberá a soma dos elementos do 
vetor A e B na sua respectiva posição. Ao final exibir os três vetores A, B e C.'''

listaa = []
listab = []
listac = []

for i in range(1,11,1):
    num = int(input(f"Informe o {i}° valor da lista A: "))
    listaa.append(num)
    
    
    
for i in range(1,11,1):
    num = int(input(f"Informe o {i}° valor da lista B: "))
    listab.append(num)
    
listac = sum(listaa + listab)

print(f"Valores da lista A: {listaa}")
print(f"Valores da lista B: {listab}")
print(f"Soma dos valores da lista A e B: {listac}")