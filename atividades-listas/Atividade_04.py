'''4) - Desenvolva um programa em python que leia valores inteiros para o vetor A e construa outro vetor B da seguinte forma:
    VETOR - A [3,  8,   4,  2,  ...,  10]
    VETOR - B [9,  4,  12,  1,  ...,  5]'''

a = []
b = []

for i in range(1,7,1):
    num = int(input(f"Digite o {i} valor: "))
    a.append(num)
    print(a)
    b.append(a[-1] * 3)
    print(b)
    num = int(input(f"Digite o {i} valor: "))
    a.append(num)
    print(a)
    b.append(a[-1] / 2)
    print(b)