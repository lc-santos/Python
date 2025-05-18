'''05) - Escrever um algoritmo para uma empresa que decide dar um reajuste a seus 584 funcionários de acordo com os seguintes critérios:
	  a) 50% para aqueles que ganham menos do que três salários mínimos;
	  b) 20% para aqueles que ganham entre três até dez salários mínimos;
	  c) 15% para aqueles que ganham acima de dez até vinte salários mínimos;
	  d) 10% para os demais funcionários.
	  Leia o nome do funcionário, seu salário e o valor do salário mínimo.
	  Calcule o seu novo salário reajustado.
	  Escrever o nome do funcionário, o reajuste e seu novo salário. Calcule quanto à empresa vai aumentar sua folha de pagamento.'''

for i in range(584):

    nome = str(input("Qual seu nome?: "))
    salario = float(input("Qual seu salário"))
    sminimo = float(input("Quanto está o salário mínimo?:"))

    cinquenta = salario * ( 50 / 100)
    vinte = salario * ( 20 / 100)
    quinze = salario * ( 15 / 100)
    dez = salario * ( 10 / 100)

    if salario < sminimo * 3:
        print(f"Seu reajuste será de 50%, {salario} + {cinquenta} = {salario+cinquenta}" )
    if salario > sminimo * 3 and salario < sminimo * 10:
        print(f"Seu reajuste será de 20%, {salario} + {vinte} = {salario+vinte}")
    if salario > sminimo * 10 and salario < sminimo * 20:
        print(f"Seu reajuste será de 15%, {salario} + {quinze} = {salario+quinze}")
    if salario > sminimo * 20:
        print(f"Seu reajuste será de 10%, {salario} + {dez} = {salario+dez}")
