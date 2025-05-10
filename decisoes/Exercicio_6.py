print(
    "Codigos dos lanches \n 100 - X-Salada com coca-cola \n 200 - Hot-dog com suco de laranja \n 300 - Sanduiche natural com suco de uva \n 400- Misto quente com fanta laranja \n 500- Pão com manteiga com café \n 600 - Pão com manteiga na chapa com café com leite")
lanche = int(input("Digite o codigo do lanche: "))

if lanche == 100:
    print("X-Salada com coca-cola")

else:
    if lanche == 200:
        print("Hot-dog com suco de laranja")

    if lanche == 300:
        print("Sanduiche natural com suco de uva")

    else:
        if lanche == 400:
            print("Misto quente com fanta laranja")

        else:
            if lanche == 500:
                print("Pão com manteiga com café")
            else:
                if lanche == 600:
                    print("Pão com manteiga na chapa com café com leite ")
                else:
                    print("Comando inválido")