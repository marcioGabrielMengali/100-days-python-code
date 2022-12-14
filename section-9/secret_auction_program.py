import os

bids = []


def add_bid(name, bid):
    bids.append({
        'name': name,
        'bid': bid
    })


def get_winner():
    max_value = 0
    winner = {}
    for result in bids:
        # print('result',result)
        # print('Ola',bids)
        name = result['name']
        bid = result['bid']
        #print(name, bid)
        # print(bid[1])
        if bid > max_value:
            max_value = bid
            #print(f'Max Value: {max_value}')
            winner = {
                'name': name,
                'bid': bid
            }
            # print(winner)
    return winner


another_bid = 'yes'
while another_bid == 'yes':
    print('Welcome To The Secret Auction program')
    name = input('What is your name? ')
    bid = float(input('What is your bid? '))
    add_bid(name, bid)
    another_bid = input(
        "Are there any other bidders? Type ´yes' or 'no': ").lower()
    os.system('cls')
# print(bids)
# print(bids)
winner = get_winner()
print(f"The winner is {winner['name']} with a bid of {winner['bid']}")
