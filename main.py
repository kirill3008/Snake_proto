from config import *
from random import choice



class Game(object):
    def __init__(self):
        self.board = Board()
        self.create_snake(None)
        self.game_over = False

    def create_snake(self,alg=None):
        plaсe = self.board.get_free_cell()
        plaсe = [plaсe // 1000 , plaсe % 1000]
        snake = Snake(alg) 
        self.board.snakes.append([snake,plaсe])

    def create_food(self,pos=None):
        if pos is None:
            place = self.board.get_free_cell()
            plaсe = [plaсe//1000, plaсe % 1000]
        self.board.food.append(pos)

    def is_game_over(self):
        return self.game_over

    def move(self):
        for snake in self.board.snakes:
            snake[0].get_dir(self.board.snakes,self.board.food,self.board.map,snake[1])
        if len(self.snakes)==0:
            self.game_over = True
    def test_field(self):
        pass
    
    def __str__(self):

        #return '\n'.join([''.join(list(map(str,i))) for i in self.map])


class Board(object):
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
        self.snakes = []
        self.food = []
    def get_free_cell(self):
        free_index = []
        for i in range(self.width):
            for j in range(self.length):
                if self.map[i][j]==None:
                    free_index.append(i*1000 + j)
        return choice(free_index)
    


    def gen_field(self):
        pass

    def get_field(self):
        pass 

        

class Snake(object):
    def __init__(self,alg = Algorithm()):
        self.alg = alg
        self.len = 1
        self.skelet = []

    def get_struct(self):
        pass


    def get_dir(self,snakes,food,map,self_pos):
        return self.alg.get_dir(snakes,food,map,self_pos)


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


class Algorithm(object):
    def __init__(self):
        pass
    def get_dir(self,snakes,food,map,self_pos):
        direction = None
        return direction

game = Game()
while game.game_status()!=0:
    game.move()
    print(game)