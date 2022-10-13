from re import S
from exceptions import *

class Tower:
    def __init__(self, name, plates = []) -> None:
        self.name = name
        self.plates = sorted(plates, reverse=True)
    
    def __rshift__(self, other: 'Tower') -> None:
        status = 0
        try:
            if self == other:
                raise ValueError()
            plate = self.pop()
            other.push(plate)
            status = 1
            exec_msg = ''
        except InvalidMoveError:
            self.push(plate)
            exec_msg = (f'MOVIMENTO INVÁLIDO: O disco retirado da torre {self.name} é'
                  f' maior que o disco existente na torre {other.name}.')
        except EmptyTowerError:
            exec_msg = (f'MOVIMENTO INVÁLIDO: A torre {self.name} não tem discos, '
                  'portanto não é possível realizar este movimento.')
        except ValueError:
            exec_msg = (f"MOVIMENTO INVÁLIDO: o disco não está sendo movido de uma torre para outra.")
        return status, exec_msg        
        
    def push(self, value: int):
        if len(self.plates) != 0 and value > self.plates[-1]:
            raise InvalidMoveError()
        self.plates.append(value)

    def pop(self):
        if len(self.plates) == 0:
            raise EmptyTowerError()
        return self.plates.pop()

    def __getitem__(self, layer):
        try:
            return self.plates[layer - 1] * '#'
        except IndexError:
            return ''
        