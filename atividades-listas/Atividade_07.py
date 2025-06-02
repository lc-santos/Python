''' 7) - Desenvolva um programa em python que receba valores numéricos informado pelo usuário e cadastre-os em uma lista,
caso a lista já contenha o valor informado, exibir a mensagem "Valor já cadastrado". No final exiba todos os valores cadastrados.'''

lista = []
program = True


while program == True:
    num = int(input(f"Informe um número: "))
    if num not in lista:
        lista.append(num)
    else: print("Número já cadastrado")
    continuar = int(input("Deseja cadastrar mais algum número? [1] Sim [2] Não : "))
    if continuar == 1:
        continue
    if continuar == 2:
        break
    


print(lista)
