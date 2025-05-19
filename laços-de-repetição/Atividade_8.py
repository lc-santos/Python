'''Faça um algoritmo que receba o nome a idade e o sexo de dez funcionário. Para cada funcionário mostre o nome e o salário líquido:
      SEXO	IDADE	SALÁRIO LÍQUIDO
      M		>= 30	R$ 100,00
      M		< 30	R$ 50,00
      F		>= 30	R$ 200,00
      F		< 30	R$ 80,00'''

for i in range(1,10,1):
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [F] Feminino [M] Masculino ")).upper()
    
                
    if sexo == "M" and idade >= 30:
        
        salario = 100
        print(f'{nome}, Seu sálario líquido será de: R${salario}')
        loop = str(input("Deseja consultar novamente?: [S] Sim [N] Não: ")).upper()
        if loop == "S":
            continue
        if loop == "N":
            break
        else: print("Comando inválido")
        continue
    
    if sexo == "M" and idade < 30:
        salario = 50
        print(f'{nome}, Seu sálario líquido será de: R${salario}')
        loop = str(input("Deseja consultar novamente?: [S] Sim [N] Não: ")).upper()
        if loop == "S":
            continue
        if loop == "N":
            break     
        
    if sexo == "F" and idade >= 30:
        salario = 200
        print(f'{nome}, Seu sálario líquido será de: R${salario}')
        loop = str(input("Deseja consultar novamente?: [S] Sim [N] Não: ")).upper()
        if loop == "S":
            continue
        if loop == "N":
            break
        else: print("Comando inválido")
    

    if sexo == "F" and idade < 30:
        salario = 80
        print(f'{nome}, Seu sálario líquido será de: R${salario}')
        loop = str(input("Deseja consultar novamente?: [S] Sim [N] Não: ")).upper()
        if loop == "S":
            continue
        if loop == "N":
            break
        else: print("Comando inválido")
    
    