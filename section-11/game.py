import game_rules

user = {}
computer = {}

def init_game():
    user,computer = game_rules.get_initial_cards()
    print(f"Your Cards: {[card for card in user.keys()]}, current score: {sum(user.values())}")
    print(f"Computer first card: {computer.keys()}")