'''16) - Faça um algoritmo que calcule o valor da conta de luz de 30 pessoas. Sabe-se que o cálculo da conta de luz segue a tabela abaixo:
      Tipo de Cliente		Valor do KW/h
      1 (Residência)		R$ 0,60
      2 (Comércio)			R$ 0,48
      3 (Indústria)			R$ 1,29'''

for i in range (30):

  tipo = int(input("Tipo: [1] Residência [2] Comércio [3] Indústria: " ))
  hora = int(input("Qual é a quantidade de hora:? "))

  if tipo == 1:
    média = hora * 0.60
    print(f"Sua conta de luz será de {média}")

  if tipo == 2:
    media = hora * 0.48
    print(f"Sua conta de luz será de {média}")

  if tipo == 3:
    média = hora * 1.29
    print(f"Sua conta de luz será de {média}")
