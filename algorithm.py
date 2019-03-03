from random import choice

from common import *


__all__ = ["LeftAlgorithm", "RightAlgorithm", "EndlessAlgorithm", "RandomAlgorithm", "FirstStupidAlgorithm"]


class Algorithm(object):
    def __init__(self):
        pass

    def get_dir(self, game_state, snake_id):
        raise RuntimeError("Not implemented in base class")


class LeftAlgorithm(Algorithm):
    def get_dir(self,Game_state,snake_id):
        direction = 'left'
        return direction


class RightAlgorithm(Algorithm):
    def get_dir(self, game_state, snake_id):
        direction = 'right'
        return direction


class EndlessAlgorithm(Algorithm):
    def __init__(self):
        super(Algorithm, self).__init__()
        self.turn_number = -1

    def get_dir(self, game_state, snake_id):
        self.turn_number += 1
        return {
            0: "left",
            1: "left",
            2: "up",
            3: "up",
            4: "right",
            5: "right",
            6: "down",
            7: "down"
        }[self.turn_number % 8]


class RandomAlgorithm(Algorithm):
    def get_dir(self, game_state, snake_id):
        """
        occupied = []
        for i in range(len(game_state.map)):
            for j in range(len(game_state.map[0])):
                if not (type(game_state.field[i][j]) in[None,Food]):
                    occupied.append((i, j))
        """
        #bodies = sum([s[0].body() for s in game_state.snakes], [])
        #print("Bodies:", bodies)
        snake, self_pos = game_state.snake(snake_id)
        y, x = self_pos
        variants = zip(
            [(y-1, x), (y, x-1), (y+1, x), (y, x+1)],
            ['up', 'left', 'down', 'right']
        )
        variants = list(filter(lambda item: type(game_state.field[item[0][0]][item[0][1]]) in [Food, type(None)], variants))
        #print("Variants:", variants)
        if not variants:
            return 'left'
        return choice(variants)[1]


def search_min_dist(snake_coord, food_coord_list):
    cur_dist = 90000
    for coord in food_coord_list:
        new_dist = ((snake_coord[0]-coord[0])**2 + 
                    (snake_coord[1]-coord[1])**2)**0.5
        cur_dist = min(cur_dist,new_dist)
    return cur_dist


class FirstStupidAlgorithm(Algorithm):
    def __init__(self):
        super(Algorithm, self).__init__()
        self.dir_to_coord = {
            'left':(0,-1),
            'right':(0,1),
            'up':(-1,0),
            'down':(1,0)
        }
        self.inverse = {
            'left':'right',
            'right':'left',
            'up':'down',
            'down':'up'
        }
        self.last_dir = 'None'
    
    def get_dir(self,game_state,snake_id):
        food = Game_state.food
        min_dist = 9000000
        self_posit = []
        snake,pos = game_state.snake(snake_id)
        dir = choice(['left','right','up','down'])
        for i in snake.skelet:
            pos = (pos[0]+self.dir_to_coord[i][0],pos[1]+self.dir_to_coord[i][1])
            self_posit.append(pos)
        if food:
            for i in self.dir_to_coord.keys():
                new_self_coord = (self_pos[0] + self.dir_to_coord[i][0],self_pos[1] + self.dir_to_coord[i][1])
                distance = search_min_dist(new_self_coord,food)
                if distance <=min_dist and self.inverse[self.last_dir]!=i and (new_self_coord not in self_posit):
                    dir = i
                    min_dist = distance
        self.last_dir = dir 
        return dir
