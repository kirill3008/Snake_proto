from algorithm import LeftAlgorithm
from main import Game


def main():
    game = Game([(LeftAlgorithm(),[6,8])])
    print(game.board)
    while game.is_game_over()==False:
        game.move()
        print(game.board)

#cProfile.run("main()")
main()
