'''14) - Desenvolva um programa em python que leia o nome e uma nota para um aluno, crie duas listas para armazenar estes valores,
      o usuário deverá informar um nome de aluno para a pesquisar, se o aluno existir na lista com os nomes do aluno, exibir o nome e a nota do aluno,
      caso contrário informar a mensagem "Aluno não cadastrado."'''
      
aluno = []
notas = []

nome = str(input("Qual o nome do aluno?: ")).upper()
aluno.append(nome)
nota = float(input("Qual a nota desse aluno?: "))
notas.append(nota)

pesquisa = str(input("Deseja consultar a nota de qual aluno?:")).upper()
if pesquisa in aluno:
    print(f"A nota do aluno ''{pesquisa}'' é {notas}")
