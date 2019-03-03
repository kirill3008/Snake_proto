
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
