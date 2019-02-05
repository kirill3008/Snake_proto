from exceptions import InternalError

class Field(object):
    def __init__(self,row,columns):
        self.map = [['0' for i in range(columns)] for j in range(row)]
        self.snakes = []
    def get_cell(self,pos):
        return self.map[pos[0]][pos[1]]
    def add_snake(self,algorithm,pos):
        if self.get_cell(pos) == ' ':
            self.snakes.append([[pos],Snake[algorithm]])
            self.map[pos[0]][pos[1]] = 's'
        else:
            raise InternalError('field {0};{1} is not free'.format(pos[0],pos[1]))







    def __str__(self):
        return '\n'.join([''.join(row) for row in self.map])




class Snake(object):
    def __init__(self,logic,length = 1):
        self.algorithm = logic
        self.length = length




