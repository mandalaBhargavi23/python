python programs

1.
print("Hello, World!")

2. simple calculator

def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    
    if operation == "+":
        print(f"The result is: {num1 + num2}")
    elif operation == "-":
        print(f"The result is: {num1 - num2}")
    elif operation == "*":
        print(f"The result is: {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"The result is: {num1 / num2}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operation")

calculator()


3.even or odd

def check_even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

check_even_odd()

4.largest number among 3 numbers

def largest_number():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    
    if num1 >= num2 and num1 >= num3:
        print(f"The largest number is {num1}")
    elif num2 >= num1 and num2 >= num3:
        print(f"The largest number is {num2}")
    else:
        print(f"The largest number is {num3}")

largest_number()

5.factorial

def factorial():
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"The factorial of {num} is {fact}")

factorial()

6.prime number

def check_prime():
    num = int(input("Enter a number: "))
    
    if num <= 1:
        print(f"{num} is not a prime number.")
        return
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            return
    
    print(f"{num} is a prime number.")

check_prime()

7.fibonacci series

def fibonacci():
    n_terms = int(input("How many terms? "))
    n1, n2 = 0, 1
    count = 0
    
    if n_terms <= 0:
        print("Please enter a positive integer.")
    elif n_terms == 1:
        print(f"Fibonacci sequence up to {n_terms}: {n1}")
    else:
        print("Fibonacci sequence:")
        while count < n_terms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

fibonacci()

8.sum of digits

def sum_of_digits():
    num = int(input("Enter a number: "))
    sum_digits = 0
    
    while num > 0:
        sum_digits += num % 10
        num //= 10
    
    print(f"The sum of digits is {sum_digits}")

sum_of_digits()


9.count vowels of string

def count_vowels():
    string = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in string:
        if char in vowels:
            count += 1
    
    print(f"Number of vowels in the string: {count}")

count_vowels()

10.reverse a string

def reverse_string():
    string = input("Enter a string: ")
    reversed_string = string[::-1]
    print(f"Reversed string: {reversed_string}")

reverse_string()




