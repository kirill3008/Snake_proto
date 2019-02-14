from config import *
from random import choice

class Game(object):
    def __init__(self,length = FIELD_LENGTH,width = FIELD_WIDTH,field_map=FIELD_MAP_FILE):
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
        self.width = width
        self.length = length
        self.snakes = 0
        self.create_snake(None)
    def create_snake(self,alg=None):
        plaсe = self.get_free_cells()
        plaсe = [plaсe // 1000 , plaсe % 1000]
        snake = SnakeHead(alg)
        self.map[plaсe[0]][plaсe[1]] = snake 
        self.snakes.append([snake,plaсe])

    def play(self):
        pass
    def move(self):
        for snake in self.snakes:
            snake[0].get_move(self.map,snake[1])
    def get_free_cell(self):
        free_index = []
        for i in range(self.width):
            for j in range(self.length):
                if self.map[i][j]==None:
                    free_index.append(i*1000 + j)
        return choice(free_index)

    def __str__(self):

        return '\n'.join([''.join(list(map(str,i))) for i in self.map])



class SnakeHead(object):
    def __init__(self,alg = None):
        self.alg = alg
        self.len = 1

    def __str__(self):
        return '~'


    def get_move(self,map,self_pos):
        return 'up'


class Wall(object):
    def __init__(self):
        pass
    def __str__(self):
        return '#'
class Food(object):
    def __init__(self):
        pass
    def __str__(self):
        return '*'

print(Game())