# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
by_four = year/4
by_hundred = year/100
by_four_hundred = year/400

#True = Leap
#False = Not Leap
leap_year = []
leap_year.append(True) if by_four % 1 == 0 else leap_year.append(False)
leap_year.append(False) if by_hundred % 1 == 0 else leap_year.append(True)
leap_year.append(True) if by_four_hundred % 1 == 0 else leap_year.append(False)

count_true = leap_year.count(True)
count_False = leap_year.count(False)
if count_true > count_False:
    print('Leap Year.')
else:
    print('Not Leap Year')

