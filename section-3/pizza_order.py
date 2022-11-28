# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0.0
if size.upper() == 'S' and add_pepperoni.upper() == 'Y':
    bill += 17
elif size.upper() == 'S' and add_pepperoni.upper() == 'N':
    bill += 15
elif size.upper() == 'M' and add_pepperoni.upper() == 'Y':
    bill += 23
elif size.upper() == 'M' and add_pepperoni.upper() == 'N':
    bill += 20
elif size.upper() == 'L' and add_pepperoni.upper() == 'Y':
    bill += 28
elif size.upper() == 'L' and add_pepperoni.upper() == 'N':
    bill += 25
else:
    print('Error')

if extra_cheese.upper() == 'Y':
    bill += 1

print(f"Your final bill is: ${int(bill)}.")