salario = float(input("Seu salário R$: "))

if salario <= 600:
    trinta = (salario * 30 / 100) + salario
    print(f"Com seu salário de {salario} seu aumento será de 30% e seu salário será {trinta} R$")

else:
    if salario >= 600.1:
        if salario <= 1100:
            vintecinco = (salario * 25 / 100) + salario
            print(f"Com seu salário de {salario} seu aumento será de 25% e seu salário será de {vintecinco} R$ ")

        if salario >= 1100.1:
            if salario <= 2400:
                vinte = (salario * 20 / 100) + salario
                print(f"Com seu salario de {salario} seu aumento será de 20% e seu salário será de {vinte} R$")

            else:
                if salario >= 2400.1:
                    if salario <= 3550:
                        quinze = (salario * 15 / 100) + salario
                        print(f"Com seu salário de {salario} seu aumento será de 15% e seu salário será de {quinze} R$")

                    if salario >= 3550.1:
                        dez = (salario * 10 / 100) + salario
                        print(f"Com seu salário de {salario} seu aumento será de 10% e seu salário será de {dez} R$")