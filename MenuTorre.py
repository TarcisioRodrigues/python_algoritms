easy = '3'
normal = '4'
hard = '5'
veryHard = '6'
UltraHard = '8'
ndiscos=0

while True:
    print("Dificuldades :1-Easy,2-normal,3-Hard,4-VeryHard e 5-UltraVeryHard")
    ctrl = input("\nInforme o numero ")

    for i in range(100):
            if ctrl == i.__str__():
                if (ctrl == '1'):
                    ndiscos = easy
                if (ctrl == '2'):
                    ndiscos = normal
                if (ctrl == '3'):
                    ndiscos = hard
                if (ctrl == '4'):
                    ndiscos = veryHard
                if (ctrl == '5'):
                    ndiscos = UltraHard
    if ndiscos != "" and int(ndiscos) >= 3:
            print("saodjawhd")
    else:
            print('Erro')
