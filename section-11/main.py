import art
import game
import os


def init():
    play = input("Do you Want to play a game of BlackJack 'y' or 'n' ? ").lower()
    if play== 'y':
        print(art.logo)
        game.init_game()
        another_card = input("Type 'y' for another card or 'n' to pass: ").lower()
        while another_card == 'y':
            check = game.get_card('user')
            if check == 'loose':
                break
            if check == 'winner':
                break
            else:
                another_card = input("Type 'y' for another card or 'n' to pass: ").lower()
    else:
        os.system('cls')
        init()


init()