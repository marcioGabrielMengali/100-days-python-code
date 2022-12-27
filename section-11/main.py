import art
import game
import os


def init():
    play = input("Do you Want to play a game of BlackJack 'y' or 'n' ? ").lower()
    if play== 'y':
        print(art.logo)
        game.init_game()
    else:
        os.system('cls')
        init()


init()