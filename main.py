from random import choice, random
from copy import deepcopy

from algorithm import LeftAlgorithm, RightAlgorithm, Algorithm, EndlessAlgorithm
from config import *
from exceptions import InternalError

import cProfile


def discrete_random(p):
    return random() < p

class Game(object):
    def __init__(self):
        self.food = []
        self.board = Board(self.food)
        self.game_over = False

    def create_snake(self,alg=None,pos=None):
        if pos is None:
            pos = self.board.get_free_cell()
        else:
            if pos[0] < 0 or pos[1] < 0:
                raise RuntimeError("Coordinates can't be negative")

        snake = Snake(self.board.max_id,alg=alg)
        snake.eat()
        self.board.max_id +=1 
        self.board.snakes.append([snake,pos])

    def create_food(self,how_much = FOOD_PER_MOVE):
        """
        if pos is None:
            place = self.board.get_free_cell()
            #plaсe = [plaсe//1000, plaсe % 1000]
        self.board.food.append(pos)
        """
        free_cells = self.board.free_cells()
        for cell in free_cells:
            prob = how_much / len(free_cells)
            if discrete_random(prob):
                self.food.append(cell)


    def is_game_over(self):
        return self.game_over

    def move(self):
        for snake in self.board.snakes:
            direction = snake[0].move(self.board.snakes,self.board.food,self.board.map,snake[1])
            if direction == 'up':
                snake[1][0]-=1
            elif direction == 'down':
                snake[1][0]+=1
            elif direction == 'left':
                snake[1][1]-=1
            else:
                snake[1][1]+=1
        self.test_field()
        self.create_food()

        if len(self.board.snakes)==0:
            print("No more snakes")
            self.game_over = True
        print(self.board)

    def test_field(self):
        field = self.board.raw_field()
        to_kill = []
        for i in range(self.board.width):
            for j in range(self.board.length):
                #print(type(i),type(j))
                if len(field[i][j])>1:
                    in_cell_heads = []
                    can_die = False
                    in_cell_food = False
                    for k in field[i][j]:
                        if type(k) == type(SnakeHead(-1)):
                            in_cell_heads.append(k.id_snake)
                        elif type(k) in [SnakeTail, Wall]:
                            can_die = True
                        elif type(k) ==  Food:
                            in_cell_food = True
                    if in_cell_food:
                        for l in in_cell_heads:
                            for k in range(len(self.board.snakes)):
                                if l == self.board.snakes[k][0].id_snake:
                                    self.board.snakes[k][0].eat()
                        self.food.remove([i,j])
                    if len(in_cell_heads)>1 or can_die:
                        to_kill += in_cell_heads
        for i in to_kill:
            for j in range(len(self.board.snakes)):
                if i == self.board.snakes[j][0].id_snake:
                    self.board.snakes.pop(j)
                    break



class Board(object):
    def __init__(self, food, length = FIELD_LENGTH, width = FIELD_WIDTH, field_map=FIELD_MAP_FILE):
        file = open(field_map)
        self.map = []
        for lines in file.readlines():
            line = []
            for i in lines[0:-1]:
                if i == '#':
                    line.append([Wall()])
                else:
                    line.append([])
            self.map.append(line)
        self.width = width
        self.length = length
        self.snakes = []
        self.food = food
        self.max_id = 0

    def get_free_cell(self):
        """
        free_index = []
        for i in range(self.width):
            for j in range(self.length):
                if len(self.map[i][j])==0:
                    free_index.append(i*1000 + j)
        return choice(free_index)
        """
        return choice(self.free_cells())

    def free_cells(self):
        result = []
        field = self.raw_field()
        for i in range(self.width):
            for j in range(self.length):
                if len(field[i][j])==0:
                    result.append([i, j])
        return result

    def __str__(self):
        def line(lst):
            return ''.join(map(str, map(lambda x: ' ' if x is None else x, lst)))

        return '\n'.join([line(line_list) for line_list in self.field()])

    def raw_field(self):
        field = deepcopy(self.map)
        for food in self.food:
            field[food[0]][food[1]].append(Food())
        for snake in self.snakes:
            field[snake[1][0]][snake[1][1]].append(SnakeHead(snake[0].id_snake))
            for i in snake[0].body():
                field[snake[1][0]+i[0]][snake[1][1]+i[1]].append(SnakeTail())
        return field

    def field(self):
        result = self.raw_field()
        for line in result:
            for i in range(len(line)):
                lst = line[i]
                if (len(lst)) > 1:
                    raise InternalError("Too many objects in cell: {0}".format(lst))
                if line[i]:
                    line[i] = line[i][0]
                else:
                    line[i] = None
        return result


def inversed(dir):
    dic = {
        'left':'right',
        'right':'left',
        'up':'down',
        'down':'up'
    }
    return dic[dir]


class Snake(object):
    def __init__(self, id_snake, alg = Algorithm()):
        self.alg = alg
        self.len = 1
        self.skelet = []
        self.id_snake = id_snake
        self.food = 0

    def get_struct(self):
        return self.skelet

    def move(self,snakes,food,map,self_pos):
        dir = self.alg.get_dir(snakes,food,map,self_pos)
        self.skelet.insert(0,inversed(dir))
        if self.food > 0:
            self.food -= 1
        else:
            self.skelet.pop()
        return dir

    def eat(self):
        self.food += FOOD_COST


    def body(self):
        result = []
        x = 0
        y = 0
        for dir in self.skelet:
            if dir == 'up':
                x-=1
            elif dir == 'down':
                x+=1
            elif dir == 'left':
                y-=1
            else:
                y+=1
            result.append((x,y))
        return result



class Wall(object):
    def __init__(self):
        pass

    def __repr__(self):
        return '#'


class Food(object):
    def __init__(self):
        pass

    def __repr__(self):
        return '*'


class SnakeHead(object):
    def __init__(self,id_snake):
        self.id_snake = id_snake
    def __str__(self):
        return 'O'
class SnakeTail(object):
    def __init__(self):
        pass
    def __str__(self):
        return '~'



def main():
    game = Game()
    game.create_snake(alg=RightAlgorithm(), pos=[6, -5])
    game.create_snake(alg=LeftAlgorithm(), pos=[6, 8])
    print(game.board)
    while game.is_game_over()==False:
        game.move()

#cProfile.run("main()")
main()