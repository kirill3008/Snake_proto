from config import *


class Game(object):
    def __init__(self,length = FIELD_LENGTH,width = FIELD_WIDTH, snakes = COUNT_OF_SHAKES,field_map=FIELD_MAP_FILE):
        file = open(field_map)
        self.map = []
        for i in range(width):
            line = []
            for j in range(length):
                if field_map.read(1) == '#':
                    line.append(Wall())
                else:
                    line.append(None)
            self.map.append(line)

                
    def play(self):
        pass

    def __str__(self):
        return '\n'.join([''.join(i) for i in self.map])



class Snake(object):
    def __init__(self,alg = None):
        self.alg = alg
class Wall(object):
    def __init__(self):
        pass
class Food(object):
    def __init__(self):
        pass
