import os
# Funtionc - Calculator Operations


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

while True:
    os.system('cls')
    num1 = int(input("What's the first number? "))
    for symbol in operations.keys():
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What's the second number? "))
    result = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    another_operation = input(
        f"Type 'y' to continue calculation with {result}, or type 'n' to exit: ")
    while another_operation.lower() == 'y':
        operation = input("Pick an operation: ")
        next_number = int(input("What's the next number ? "))
        previous_result = result
        result = operations[operation](result, next_number)
        print(f"{previous_result} {operation} {next_number} = {result}")
        another_operation = input(
            f"Type 'y' to continue calculation with {result}, or type 'n' to exit: ")
