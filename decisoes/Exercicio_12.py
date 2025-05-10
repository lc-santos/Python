nome = input("Digite o nome do jogador: ")
idade = int(input("Qual a idade desse jogador: "))

if idade>=5:
    if idade <=10:
        print(f'Olá {nome}! Você pertence a:')
        print("Categoria Infatil")

    else:
        if idade >=11:
            if idade <=15:
                print(f'Olá {nome}! Você pertence a:')
                print("Categoria Juvenil")

            if idade >=16:
                if idade <=20:
                    print(f'Olá {nome}! Você pertence a:')
                    print("Categoria Junior")

                else:
                    if idade>=21:
                        if idade<=25:
                            print(f'Olá {nome}! Você pertence a:')
                            print("Categoria Profissional")
