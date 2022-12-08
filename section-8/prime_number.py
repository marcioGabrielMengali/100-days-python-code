# Write your code below this line 👇
def prime_checker(number):
    verify = True
    for i in range(2, n):
        if(n % i) == 0:
            verify = False
            break
    print("It's a prime number") if verify else print("It's not a prime number")


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
