from hanoi import HanoiTower
import os

def cls():
    os.system('cls')

NPLATES = [3, 4, 5, 7, 10, 15]
DESCRICAO = ['FÁCIL', 'NORMAL', 'DIFÍCIL', 'MUITO DIFÍCIL', 'ULTA DIFÍCIL', 'HARDCORE']


def get_difficulty():
    while True:
        print("======================================")
        for idx, desc in enumerate(DESCRICAO, 1):
            print(f'{idx} - {desc}')
        print("======================================")
        _in = input("Escolha a dificuldade desejada: ")
        try:
            value = int(_in)
            if value < 1 or value > len(NPLATES):
                raise ValueError()
            return value - 1
        except:
            cls()
            print(f'O input inserido não é valido, certifique-se que o valor está entre 1 e {len(NPLATES)}.')
        
def main():
    idx = get_difficulty()
    nplates = NPLATES[idx]
    descricao = DESCRICAO[idx]
    cls()
    hanoi = HanoiTower(nplates)
    hanoi.exec_msg = f"Dificuldade escolhida: {descricao} - {nplates} discos."
    while hanoi.running:
        hanoi.show()
        hanoi.execute(input("insira um comando válido, ou digite \"help\" para listar os comandos: "))
        cls()


print("Bem-vindo ao jogo da torre de Hanoi.")

while True:
    main()
    cls()
    if input('Deseja iniciar um outro jogo? (Y/N) ').upper() == 'N':
        break
cls()