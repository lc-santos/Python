'''Uma Companhia de Seguros possui nove categorias de seguro baseadas na idade e ocupação do segurado. Somente pessoas com pelo menos 17 anos e não mais de 70 anos podem adquirir apólices
de seguro. Quanto às classes de ocupações, foram definidos três grupos de risco. A tabela abaixo fornece as categorias em função da faixa etária e do grupo de risco. Dados nome, idade
e grupo de risco, determinar a categoria do pretendente à aquisição de tal seguro. Imprimir o nome a idade e a categoria do pretendente e caso a idade não esteja na faixa necessária,
imprimir uma mensagem.
	  GRUPO DE RISCO
	  IDADE		BAIXO		MEDIO		ALTO
	  17 A 20		1			2			3
	  21 A 24		2			3			4
	  25 A 34		3			4			5
	  35 A 64		4			5			6
	  65 A 70		7			8			9
'''

program = True 

while program == True:
    idade = int(input("Qual sua idade?: "))
    ocupacao = int(input("Qual sua ocupação?: [1] Baixo [2] Médio [3] Alto: "))
    
    if idade < 17:
        print("Idade abaixo do necessário")
        continue

    if idade >= 17 or idade <= 20:
        if ocupacao == 1:
            print("Aprovado")
        if ocupacao == 2:
            print("Meio Aprovado")
        if ocupacao == 3:
            print("Negado")
    else: print("Comando inválido")
   
    if idade >= 21 or idade <= 24:
        if ocupacao == 1:
            print("Aprovado")
        if ocupacao == 2:
            print("Meio Aprovado")
        if ocupacao == 3:
            print("Negado")
    else: print("Comando inválido")
	
	
    if idade >= 25 or idade <= 34:
        if ocupacao == 1:
            print("Aprovado")
        if ocupacao == 2:
            print("Meio Aprovado")
        if ocupacao == 3:
            print("Negado")
   
   