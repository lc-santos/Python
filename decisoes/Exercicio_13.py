
valorcompra = float(input("Qual foi o valor da compra?: "))

print("Qual a forma de pagamento?: ")
print("[1] A vista")
print("[2] A prazo 30 dias")
print("[3] A prazo 60 dias")
print("[4] A prazo 90 dias")
print("[5] Cartão de debito")
print("[6] Cartão de crédito")
escolha = int(input(": "))

desconto10 = (valorcompra * 10 / 100)
desconto5 = (valorcompra * 5 / 100)
acres5 = (valorcompra * 5 / 100)
acres8 = (valorcompra * 8 / 100)
acres7 = (valorcompra * 7 / 100)


if escolha == 1:
    print(valorcompra - desconto10)
else:
    if escolha == 2:
        print(valorcompra - desconto5)
    else:
        if escolha == 3:
            print(valorcompra)
        else:
            if escolha == 4:
                print(valorcompra + acres5)
            else:
                if escolha == 5:
                    print(valorcompra + acres8)
                else:
                    if escolha == 6:
                        print(valorcompra + acres7)
