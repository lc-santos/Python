time1 = str(input("Primeiro time: "))
gols1 = int(input("Gols do primeiro time: "))

time2 = str(input("Segundo time: "))
gols2 = int(input("Gols do segundo time: "))

if gols1 > gols2:
    print(f'{time1} ganhou!!')
else:
    if gols2 > gols1:
     print(f'{time2} Ganhou!!')
    else: 
        if gols1 == gols2:
            print("Empate")
