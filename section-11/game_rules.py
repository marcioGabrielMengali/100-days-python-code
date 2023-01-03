import give_cards


def get_initial_cards(dict_user,dict_computer):
    for i in range(2):
        give_cards.select_card(dict_user)
        give_cards.select_card(dict_computer)

def check_values(dict):
    value = sum(dict.values())
    if value > 21:
        return 'loose'
    if value == 21:
        return 'winner'
    else:
        return 'stop'

