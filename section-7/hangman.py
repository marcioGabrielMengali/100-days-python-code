from random import randint

#list of wordsss
word_list = ['ardvark', 'baboon', 'camel']

#function to random choose a word
def chose_word():
    return word_list[randint(0,len(word_list)-1)]

#function to verify the stages in the game
def verify_stages(guees, chosen_word, stage):
    return stage if guees in chosen_word else stage-1


#function to verify the letter in the choosen word
def verify_letter(chosen_word, word, word_list,stage):
    for i, letter in enumerate(chosen_word):
        word_list[i] = word.lower() if letter.lower() == word.lower() else word_list[i]
    stage = verify_stages(word, chosen_word, stage)
    return (word_list,stage)

#function to generate white spaces
def create_white_spaces(chosen_word):
    word_list = ['_' for x in chosen_word]
    return word_list



        

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#init
chosen_word = chose_word()
print(chosen_word)
word_list = create_white_spaces(chosen_word)
stage = len(stages)-1


#intorduction
print('Welcome To The Hangman Game')
print(f'Your Word has {len(chosen_word)} letters\n')
print(' '.join(word_list))
print(stages[stage])

while '_' in word_list:
    word = input('Guess a Letter: ')
    word_list, stage = verify_letter(chosen_word,word,word_list,stage)
    print(' '.join(word_list))
    print(stages[stage])
    if stage == 0:
        print('You Loose')
        print(f'The word is {chosen_word}')
        break;
print('You Win') if stage != 0 else 'End Game'




