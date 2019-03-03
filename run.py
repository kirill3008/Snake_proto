from algorithm import *
from main import Game


def main():
    game = Game([(FirstStupidAlgorithm(),[6, 8])])
    print(game.board)
    while game.is_game_over()==False:
        game.move()
        print(game.board)

#cProfile.run("main()")
main()
