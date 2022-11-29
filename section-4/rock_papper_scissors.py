import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
list_of_choices = [rock, paper, scissors]
choose = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ')
random_number = random.randint(0,2)
choose = int(choose)
print(list_of_choices[choose])
print('X')
print(list_of_choices[random_number])

if choose == 0 and random_number == 2:
    print('You Win!!')
elif choose == 2 and random_number == 1:
    print('You Win!!')
elif choose == 1 and random_number == 0:
    print('You Win!!')
else:
    print('You Loose!')