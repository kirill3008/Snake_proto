from config import *
from random import choice
from copy import deepcopy


class Game(object):
    def __init__(self):
        self.board = Board()
        self.create_snake(None)
        self.game_over = False

    def create_snake(self,alg=None,pos=None):
        if pos is None:
            plaсe = self.board.get_free_cell()
            plaсe = [plaсe // 1000 , plaсe % 1000]
        snake = Snake(alg = alg,self.board.max_id)
        self.board.max_id +=1 
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
            direction = snake[0].get_dir(self.board.snakes,self.board.food,self.board.map,snake[1])
            if direction == 'left':
                snake[1][0]-=1
            elif direction == 'right':
                snake[1][0]+=1
            elif direction == 'up':
                snake[1][1]-=1
            else:
                snake[1][1]+=1
        self.test_field()

        if len(self.snakes)==0:
            self.game_over = True
    def test_field(self):
        field = self.board.get_field()
        to_kill = []
        for i in range(self.board.width):
            for j in range(self.board.length):
                if len(field[i][j])>1:
                    in_cell_heads = []
                    can_die = False
                    for i in field[i][j]:
                        if type(i) = type(SnakeHead(-1)):
                            in_cell_heads.append(i.id)
                        elif type(i) = type(SnakeTail()):
                            can_die = True
                    if len(in_cell_heads)>1 or can_die:
                        to_kill += in_cell_heads
        for i in to_kill:
            for j in range(len(self.board.snakes)):
                if i = j[0].id:
                    self.board.snakes.pop(j)
                    break



    
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
                    line.append([Wall()])
                else:
                    line.append([None])
            self.map.append(line)
        self.width = width
        self.length = length
        self.snakes = []
        self.food = []
        self.max_id = 0
    def get_free_cell(self):
        free_index = []
        for i in range(self.width):
            for j in range(self.length):
                if self.map[i][j][0]==None:
                    free_index.append(i*1000 + j)
        return choice(free_index)
    


    def gen_field(self):
        field = deepcopy(self.map)
        for food in self.food:
            if 
            field[food[0]][food[1]].append(Food())
        for snake in self.snakes:
            field[snake[1][0]][snake[1][1]].append(SnakeHead(id))
            for i in snakes[0].get_struct():
                pass
        return field
    def get_field(self):
        pass 

        

class Snake(object):
    def __init__(self,alg = Algorithm(),id):
        self.alg = alg
        self.len = 1
        self.skelet = []
        self.id = id

    def get_struct(self):
        return self.skelet


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
class SnakeHead(object):
    def __init__(self,id):
        self.id
    def __str__(self):
        return 'O'
class SnakeTail(object):
    def __init__(self):
        pass
    def __str__(self):
        return '~'




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