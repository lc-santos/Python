nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota:"))

media = ((n1 + n2) + n3) / 3

print(f'Olá {nome}!')
print(f'Sua média foi: {media}')

if media >= 7:
    print("Aprovado!")

else:
    if media <= 5:
        print("Reprovado")
    else:
        if media>=5.01:
            if media <=6.9:
                print("Recuperação")