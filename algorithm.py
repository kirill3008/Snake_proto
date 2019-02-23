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
