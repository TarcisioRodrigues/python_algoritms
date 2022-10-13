from datetime import datetime
from time import sleep, time
from tower import Tower
import re
import os

def cls():
    os.system('cls')

FRAME_FREEZE = 0.7 * 3

class HanoiTower:
    def __init__(self, n_plates, from_solver=False) -> None:
        if n_plates > 24:
            raise ValueError('O valor máximo de discos é 20.')
        size = os.get_terminal_size()
        
        if n_plates > (size.lines - 9):
            self.layers = range(n_plates, 0, -1)
        else:
            self.layers = range(size.lines - 9, 0, -1)
        self.nplates = n_plates
        self.length = (size.columns - 9)//3
        self.A = Tower('A', map(lambda x: self.length - x, range(1, n_plates * 2, 2)))
        self.B = Tower('B')
        self.C = Tower('C')
        self.__surrender = False
        self.__try = 0
        self.__ts = datetime.now()
        self.from_solver = from_solver
        self.exec_msg = ''
        
    @staticmethod
    def __solver(n, source, auxiliary, destination):
        if n>0:
            yield from HanoiTower.__solver(n-1, source, destination, auxiliary)
            yield n, source, destination
            yield from HanoiTower.__solver(n-1, auxiliary, source , destination)
            
    def __repr__(self) -> str:
        result = [['Torre A', 'Torre B', 'Torre C'], ['-'*(self.length)]*3]
        for layer in self.layers:
            
            res = [self.A[layer], self.B[layer], self.C[layer]]
        
            result.append(res)
        return '\n'.join(' | '.join(n.center(self.length) for n in r) for r in result)

    @property
    def running(self):
        return not self.__surrender and not self.solved
    
    @property
    def solved(self):
        return (len(self.C.plates) == self.nplates) and not self.from_solver
    
    @property
    def stats(self):
        return f"{self.__try} movimento(s), em {datetime.now() - self.__ts}"
    
    def reset(self):
        """retorna o jogo para o estado inicial\n>>> reset"""
        self.__surrender = False
        self.A = Tower('A', map(lambda x: self.length - x, range(1, self.nplates * 2, 2)))
        self.B = Tower('B')
        self.C = Tower('C')
        self.__try = 0
        self.__ts = datetime.now()
        self.exec_msg = '[RESET] jogo reiniciado para o estado inicial!'
        return self
    
    def solve(self):
        """mostra passo a passo para a resolução do problema da torre de hanoi.\n>>> solve"""
        
        self.__surrender = True
        hanoi = HanoiTower(self.nplates, from_solver=True)
        cls()
        hanoi.exec_msg = f'[!] Solução para a torre de hanoi com {self.nplates} discos.'
        hanoi.show()
        input('Pressione ENTER para visualizar a resolução.')
        
        for i, (n, src, dst) in enumerate(HanoiTower.__solver(self.nplates, *'ABC'), 1):
            cls()
            hanoi.exec_msg = f'{i}. Mova o disco {n} da torre {src} para a torre {dst}.'
            hanoi.execute(f'move {src} {dst}').show()
            
            if i < 2 ** self.nplates - 1:
                input('Pressione ENTER para ir para o próximo movimento.')
        input('Torre resolvida, pressione ENTER para voltar para o MENU.')
        
        return self
    
    def move(self, src: str, dst: str):
        """move um disco de uma torre para a outra, especificando a origem e o destino do disco.\n>>> move {A|B|C} {A|B|C}"""
        
        if not self.running:
            print("A torre não está mais em execução, reinicie com o comando \"reset\" para mover qualquer disco.")
            return self
        
        try:
            src: Tower = getattr(self, src.upper())
            dst: Tower = getattr(self, dst.upper())
        except:
            self.exec_msg = "A torre não existe, ou o argumento passado está incorreto de alguma forma. Digite \"help move\" para visualizar o uso do comando."
            return self
        status, exec_msg= src >> dst
        self.__try += status
        
        if status == 0:
            self.exec_msg = exec_msg
        if self.solved:
            self.exec_msg = f"[TORRE FINALIZADA] Parabéns, você finalizou esta torre de hanoi com {self.stats}."
            self.show()
            input("Pressione ENTER para continuar.")
            cls()
        return self
    
    def execute(self, command: str):
        if not command:
            return self
        
        cls()
        
            
        cmd, *args = command.strip().split()
        result = self.commands.get(cmd, None)
        
        if result is None:
            print("Comando inexistente/inválido, tente um dos listados abaixo:")
            self.help()
        else:
            try:
                result(self, *args)
            except:
                self.exec_msg = f"O comando foi inserido de forma errada, utilize \"help {cmd}\" para visualizar o uso correto."
                
        return self

    def show(self):
        if not self.from_solver and not self.solved:
            stats = f'TENTATIVAS: {self.__try}\nTEMPO DECORRIDO: {datetime.now() - self.__ts}'
        else:
            stats = self.exec_msg
            self.exec_msg = ''
        
        print(
            self, 
            '\n',
            self.exec_msg, 
            stats,
            sep='\n'
        )
        self.exec_msg = ''
        return self

    def help(self, command:str = None):
        """mostra informação sobre o comando fornecido e como utilizá-lo.\n>>> help [COMANDO]"""
        if command is None:
            for key, value in self.commands.items():
                print(f'{key} - {value.__doc__}')
        else:
            cmd = self.commands.get(command.strip(), None)
            
            if cmd is None:
                print("Comando inválido/inválido, tente um dos listados abaixo:")
                self.help()
            else:
                print(cmd.__doc__)
        input("Pressione ENTER para continuar.")
    
    def exit(self):
        """finaliza o jogo atual e retorna ao menu inicial do programa.\n>>> exit"""
        self.__surrender = True
        self.exec_msg = f"Jogo finalizado, com {self.stats}"
        return self
    
    commands = {
        "move": move,
        "reset": reset,
        "exit": exit,
        "solve": solve,
        "help": help,
    }

ht = HanoiTower(2)

cls()

