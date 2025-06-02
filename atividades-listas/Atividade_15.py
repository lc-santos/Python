'''15) - [DESAFIO] Desenvolva um procurado em python que leia valores inteiros para um vetor de 20 posições e mostre-o. Em seguida, troque o primeiro elemento pelo o último, 
o segundo com o penúltimo,o terceiro com o antepenúltimo e,assim, sucessivamente. Mostre o novo vetor após todas as trocas. '''

lista = []
remove = []

for i in range(1,4,1):
    num = int(input(f"Informe o {i} valor: "))
    lista.append(num)

print(f"A lista em ordem normal {lista}")

for i in range(1,4,1):
    remove = lista.pop(0)
    lista.insert(-1,remove)
    


print(f"A lista em ordem do desafio {lista}")
