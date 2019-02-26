from random import choice


__all__ = ["LeftAlgorithm", "RightAlgorithm", "EndlessAlgorithm", "RandomAlgorithm", "FirstStupidAlgorithm"]


class Algorithm(object):
    def __init__(self):
        pass

    def get_dir(self,Game_state,self_pos,self_struct):
        raise RuntimeError("Not implemented in base class")


class LeftAlgorithm(Algorithm):
    def get_dir(self,Game_state,self_pos,self_struct):
        direction = 'left'
        return direction


class RightAlgorithm(Algorithm):
    def get_dir(self,Game_state,self_pos,self_struct):
        direction = 'right'
        return direction


class EndlessAlgorithm(Algorithm):
    def __init__(self):
        super(Algorithm, self).__init__()
        self.turn_number = -1

    def get_dir(self,Game_state,self_pos,self_struct):
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
    def get_dir(self, snakes,food,map,self_pos,self_struct):
        print("Snakes:", snakes)
        walls = []
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j]:
                    walls.append((i, j))
        bodies = sum([s[0].body() for s in snakes], [])
        y, x = self_pos
        variants = zip(
            [(y-1, x), (y, x-1), (y+1, x), (y, x+1)],
            ['up', 'left', 'down', 'right']
        )
        variants = list(filter(lambda item: not item[0] in bodies and not item[0] in walls, variants))
        if not variants:
            return 'left'
        print("Variants:", variants)
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
    
    def get_dir(self,Game_state,self_pos,self_struct):
        food = Game_state.food
        min_dist = 9000000
        self_posit = []
        pos = self_pos
        dir = choice(['left','right','up','down'])
        for i in self_struct:
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
