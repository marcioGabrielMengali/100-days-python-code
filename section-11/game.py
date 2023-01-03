import game_rules
import give_cards

user = {}
computer = {}

def init_game():
    game_rules.get_initial_cards(dict_user=user,dict_computer=computer)
    print(f"Your Cards: {[card for card in user.keys()]}, current score: {sum(user.values())}")
    print(f"Computer first card: [ {list(computer.keys())[0]}, ?], current score: {list(computer.values())[0]}")


def get_card(player):
    if player == 'user':
        give_cards.select_card(user)
        print(f"Your Cards: {[card for card in user.keys()]}, current score: {sum(user.values())}")
        loose = game_rules.check_values(user)
        if loose == 'loose':
            print('You Loose!')
            print(f"Computer Cards: {[card for card in computer.keys()]}, current score: {sum(computer.values())}")
            return 'loose'
        if loose == 'winner':
            print('You Winnnn!!')
            print(f"Your Cards: {[card for card in user.keys()]}, current score: {sum(user.values())}")
            print(f"Computer Cards: {[card for card in computer.keys()]}, current score: {sum(computer.values())}")
            return 'winner'


#Faltan Implementar esta função
def get_computer_cards():