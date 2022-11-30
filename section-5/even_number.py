#Write your code below this row 👇
total = 0
for number in range(1, 101):
    total += number if number % 2 == 0 else 0
print(total) 