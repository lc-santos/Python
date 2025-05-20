'''15) - A escola “APRENDER” faz o pagamento de seus professores por hora/aula. Faça um algoritmo que calcule e exiba o salário do professor.
 Sabe-se que o valor da hora/aula segue a tabela abaixo:
      Professor Nível 1 R$12,00 por hora/aula
      Professor Nível 2 R$17,00 por hora/aula
      Professor Nível 3 R$25,00 por hora/aula
      A escola "APRENDER” possui 50 professores.'''

for i in range(51):
    nivel = int(input("Qual seu nível?: [1] 1 [2] 2 [3] 3: "))
    horas = int(input("Quantas horas?: "))

    if nivel == 1:
        valor = 12
        salario = valor * horas
        print(f"Seu salário será de R${salario}")

    if nivel == 2:
        valor = 17
        salario = valor * horas
        print(f"Seu salário será de R${salario}")

    if nivel == 3:
        valor = 25
        salario = valor * horas
        print(f"Seu salário será de R${salario}")
