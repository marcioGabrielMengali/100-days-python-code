import string
import random

print('*#### Password Generator ####*')
letters = int(input('How many letters would you like in your password? '))
symbols = int(input('How many symbols would you like? '))
numbers = int(input('How many numbers would you like? '))
print('---------- GENERATING PASSWORD WITH : ')
print(f'{letters} letters,')
print(f'{symbols} symbols and')
print(f'{numbers} numbers.')


#create password
password = ''
i = 1
while(i <= letters):
    letter = random.choice(string.ascii_letters)
    password += letter
    i+=1
i = 1
i = 1
while(i <= symbols):
    symbol = random.choice(string.punctuation)
    password += symbol
    i+=1
while(i <= numbers):
    number = random.choice(string.digits)
    password += str(number)
    i+=1
password = random.sample(password,len(password))
random_password = "".join(password)
print(f"Your Password is: {random_password}")
