from random import choice
class Algorithm(object):
    def __init__(self):
        pass

    def get_dir(self,snakes,food,map,self_pos):
        raise RuntimeError("Not implemented in base class")


class LeftAlgorithm(Algorithm):
    def get_dir(self,snakes,food,map,self_pos):
        direction = 'left'
        return direction


class RightAlgorithm(Algorithm):
    def get_dir(self,snakes,food,map,self_pos):
        direction = 'right'
        return direction


class EndlessAlgorithm(Algorithm):
    def __init__(self):
        super(Algorithm, self).__init__()
        self.turn_number = -1

    def get_dir(self,snakes,food,map,self_pos):
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


def search_min_dist(snake_coord, food_coord_list):
    cur_dist = ((snake_coord[0]-food_coord_list[0][0])**2 + 
                (snake_coord[1]-food_coord_list[0][1])**2)**0.5
    for coord in food_coord_list[1:0]:
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
    
    def get_dir(self,snakes,food,map,self_pos):
        min_dist = 9000000
        if food:
            for i in self.dir_to_coord.keys():
                new_self_coord = (self_pos[0] + self.dir_to_coord[i][0],self_pos[1] + self.dir_to_coord[i][1])
                distance = search_min_dist(new_self_coord,food)
                if distance <=min_dist and self.inverse[self.last_dir]!=i:
                    dir = i
                    min_dist = distance
        else:
            dir =  choice(['left','right','up','down'])
        self.last_dir = dir
        return dir
            
            












