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
cliente = 0

while program == True:
	nome = str(input("Seu nome: "))
	idade = int(input("Sua idade: "))
 
	if idade >= 17 or idade <= 70:
         if idade <= 20:
            risco = str(input("Seu grupo de risco: [B] Baixo [M] Médio [A] Alto: ")).upper()
            if risco == "B":
             cliente = 1
             print(f"{nome}, sua apólice foi aprovada!, categoria {cliente}")
            if risco == "M":
             cliente = 2
             print(f"{nome}, sua apólice esta em analise!, categoria {cliente} [Saiba mais]")
            if risco == "A":
             cliente = 3
             print(f"{nome}, sua apólice foi negada!, categoria {cliente}")
         
         if idade >= 21 and idade <= 24:
            risco = str(input("Seu grupo de risco: [B] Baixo [M] Médio [A] Alto: ")).upper()
            if risco == "B":
             cliente = 2
             print(f"{nome}, sua apólice foi aprovada!, categoria {cliente}")
            if risco == "M":
             cliente = 3
             print(f"{nome}, sua apólice esta em analise!, categoria {cliente} [Saiba mais]")
            if risco == "A":
             cliente = 4
             print(f"{nome}, sua apólice foi negada!, categoria {cliente}")
        
         if idade >= 25 and idade <= 34:
            risco = str(input("Seu grupo de risco: [B] Baixo [M] Médio [A] Alto: ")).upper()
            if risco == "B":
             cliente = 3
             print(f"{nome}, sua apólice foi aprovada!, categoria {cliente}")
            if risco == "M":
             cliente = 4
             print(f"{nome}, sua apólice esta em analise!, categoria {cliente} [Saiba mais]")
            if risco == "A":
             cliente = 5
             print(f"{nome}, sua apólice foi negada!, categoria {cliente}")
             
         if idade >= 34 and idade <= 64:
            risco = str(input("Seu grupo de risco: [B] Baixo [M] Médio [A] Alto: ")).upper()
            if risco == "B":
             cliente = 4
             print(f"{nome}, sua apólice foi aprovada!, categoria {cliente}")
            if risco == "M":
             cliente = 5
             print(f"{nome}, sua apólice esta em analise!, categoria {cliente} [Saiba mais]")
            if risco == "A":
             cliente = 6
             print(f"{nome}, sua apólice foi negada!, categoria {cliente}")
        
         if idade >= 65 and idade <= 70:
            risco = str(input("Seu grupo de risco: [B] Baixo [M] Médio [A] Alto: ")).upper()
            if risco == "B":
             cliente = 7
             print(f"{nome}, sua apólice foi aprovada!, categoria {cliente}")
            if risco == "M":
             cliente = 8
             print(f"{nome}, sua apólice esta em analise!, categoria {cliente} [Saiba mais]")
            if risco == "A":
             cliente = 9
             print(f"{nome}, sua apólice foi negada!, categoria {cliente}")
    
       