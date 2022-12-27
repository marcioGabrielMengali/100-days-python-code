import give_cards

user = {}
computer = {}

def get_initial_cards():
    for i in range(2):
        user = give_cards.select_card(player = 'user')
        computer = give_cards.select_card(player = 'computer')
    return (user,computer)