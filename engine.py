from exceptions import InternalError

class Field(object):
    def __init__(self,row,columns):
        self.map = [['0' for i in range(columns)] for j in range(row)]
        self.snakes = []
    def get_cell(self,pos):
        return self.map[pos[0]][pos[1]]
    def add_snake(self,algorithm=None,pos):
        if self.get_cell(pos) == ' ':
            self.snakes.append([[pos],Snake(algorithm)])
            self.map[pos[0]][pos[1]] = 's'
        else:
            raise InternalError('field {0};{1} isn\'t free'.format(pos[0],pos[1]))
    def make_move(self):
        dead = []
        for i in range(len(self.snakes)):
            snake=self.snakes[i]
            new_position = snake[1].get_move(head_position)
            if len(snake[0])<snake[1].length:
                snake[0].insert(0,new_position)
            else:
                snake[0].insert(0,new_position)
                snake[0].pop(-1)
            if self.map[snake[0][0][0]][snake[0][0][1]]=='f':
                snake[1].length+=1
            elif self.map[snake[0][0][0]][snake[0][0][1]] == 's':
                dead.append(i)
            self.map[snake[0][0][0]][snake[0][0][1]] ='s'
        for i in reversed(dead):
            self.snakes.pop(i) 

    def create_food(self,pos):
        self.map[pos[0]][pos[1]] = 'f'  







    def __str__(self):
        return '\n'.join([''.join(row) for row in self.map])




class Snake(object):
    def __init__(self,logic = None ,length = 1):
        self.algorithm = logic
        self.length = length
    def get_move(self,head_position):
        pass







