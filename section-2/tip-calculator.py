#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total_bill = 0
tip = 0
split = 0
print('Welcome To the tip calculator!')
total_bill = float(input('Whats was the total bill? $'))
tip = int(input('How much tip would you like to give? 10, 12 or 15? '))
split = int(input('How Many people to split the bill? '))
payment = round((total_bill/split) * ((tip/100) + 1),2)
print(f'Each person should pay: ${payment}')