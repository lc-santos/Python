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
    print(salario)
elif sexo == "M" and idade < 30:
    salario = 50
    print(salario)
else: print("Comando inválido")

if sexo == "F" and idade >= 30:
    salario = 200
    print(salario)
else: print("Comando inválido")

elif sexo == "F" and idade < 30:
    salario = 80
    print(salario)

