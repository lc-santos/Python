'''02) - Escrever um algoritmo que leia os dados de “N” pessoas (nome, dade e saúde) e informe se está apta ou não para cumprir o serviço militar obrigatório. Informe os totais.'''

contador = 1
cadastro = True

while cadastro == True:
    nome = str(input("Qual seu nome?: "))
    idade = int(input("Qual sua idade?: "))
    saude = str(input("Possui problemas de saúde?: [S] [N] ")).upper()
    
    if idade >= 80:
        print("Opa, você já passou da idade de se alistar, descanse guerreiro(a)!")
        nova = int(input("Deseja consultar novamente? [1] Sim [2] Não: "))
        if nova == 1:
            contador += 1
            continue
        if nova == 2: 
            print("Ok, número de consultas: {}".format(contador))
            break
    
    if idade >= 18 and saude == "N":
        
            print("Parabéns, {}! Você esta apto para cumprir o serviço militar".format(nome))
            nova = int(input("Deseja consultar novamente? [1] Sim [2] Não: "))
            if nova == 1:
                contador += 1
                continue
            if nova == 2: 
                print("Ok, número de consultas: {}".format(contador))
                break
            
    if saude == "S" or idade < 18:
        print("Que pena {}, Você não esta apto".format(nome))
        nova = int(input("Deseja consultar novamente? [1] Sim [2] Não: "))
        if nova == 1:
            contador += 1
            continue
        if nova == 2: 
            print("Ok, número de consultas: {}".format(contador))
            break
            

            
    
    
    
        