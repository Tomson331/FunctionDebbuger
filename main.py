# P-101-l04
# 6.1 What is Function, Really?
# Functions Are Values

Python
3.11
.4(tags / v3
.11
.4: d2340ef, Jun
7
2023, 05: 45:37) [MSC v.1934 64 bit(AMD64)]
on
win32
Type
"help", "copyright", "credits" or "license()"
for more information.
    len
< built - in function
len >
type(len)
<

class 'builtin_function_or_method'>


len = "I', not the len you're looking for."
len
"I', not the len you're looking for."
type(len)
<

class 'str'>


del len
len
< built - in function
len >

# Typing just the name doesn't execute the function.
# IDLE inspects the variable as usual.
len
< built - in function
len >

# Use parentheses to call the finction.
len()
Traceback(most
recent
call
last):
File
"<pyshell#13>", line
1, in < module >
len()
TypeError: len()
takes
exactly
one
argument(0
given)

num_letters = len("four")
num_letters = 4

return_value = print("What do I return?")
What
do
I
return?
return_value

type(return_value)
<

class 'NoneType'>


print(return_value)
None


# The Anatomy of Function
def multiply(x, y):  # Function signature
    # Function body
    product = x * y
    return product


print("Where am I?")  # Not in the function body.
Where
am
I?
print("Where am I?")  # Not in the function body.

SyntaxError: unexpected
indent


def multiply(x, y)
    SyntaxError: incomplete
    input


SyntaxError: incomplete
input
SyntaxError: incomplete
input


def multiply(x, y):
    product = x * y
    return product  # Indented with one extra space.


SyntaxError: unexpected
indent


def multiply(x, y):
    product = x * y


return product  # Indented less than prevoius line.
SyntaxError: unindent
does
not match
any
outer
indentation
level


def multiply(x, y):
    product = x * y
    return product
    print("You can't see me!")


multiply(2, 4)
8

num = multiply(2, 4)
print(num)
8


def multiply(x, y)
    SyntaxError: incomplete
    input


def multiply(2, 4):


SyntaxError: invalid
syntax


def multiply(x, y):
    product = x * y
    return product


num = multiply(2, 4):

SyntaxError: incomplete
input
num = multiply(2, 4)
print(num)
8


def multiply(2, 4):


SyntaxError: invalid
syntax
product = x * y
Traceback(most
recent
call
last):
File
"<pyshell#64>", line
1, in < module >
product = x * y
NameError: name
'x' is not defined


def multiply(x, y):
    product = x * y
    return product


num = multiply(2, 4)
print(num)
8


def greet(name):
    print(f"Hello, {name}!)


SyntaxError: incomplete
input


def greet(name):
    print(f"Hello, {name}!")
    greet("Dave")


return_value = greet("Dave")
Hello, Dave!
Hello, Dave!

Traceback(most
recent
call
last):
File
"<pyshell#79>", line
1, in < module >
return_value = greet("Dave")
File
"<pyshell#78>", line
3, in greet
greet("Dave")
File
"<pyshell#78>", line
3, in greet
greet("Dave")
File
"<pyshell#78>", line
3, in greet
greet("Dave")
[Previous line repeated 1011 more times]
File
"<pyshell#78>", line
2, in greet
print(f"Hello, {name}!")
RecursionError: maximum
recursion
depth
exceeded
while pickling an object

help(len)
Help
on
built - in function
len in module
builtins:

len(obj, /)
Return
the
number
of
items in a
container.

help(multiply)
Help
on
function
multiply in module
__main__:

multiply(x, y)


def multiply(x, y):
    """Return the product of two numbers x and y."""
    product = x * y
    return product


help(multiply)
Help
on
function
multiply in module
__main__:

multiply(x, y)
Return
the
product
of
two
numbers
x and y.

# 6.2 - Write Your Own Functions
# Solutions to review exercises

# Exercise 1
def cube(num):
    """Return the cube of the input number."""
    cube_num = num**3  # Could also use pow(num, 3)
    return cube_num

print(f"0 cubed is {cube(0)}")
print(f"2 cubed is {cube(2)}")

# Exercise 2
def greet(name):
    """Display a greeting."""
    print(f"Hello {name}!")

greet("Guido")

# 6.3 Challenge: Convert Temperatures

convert_cel_to_far()
F - C * 9/5 + 32
convert_far_to_cel()
C - (F - 32) * 5/9

Enter a temperature in degress F: 72
72 degress F - 22.22 degrees C

# 6.4. Run in Circles

n = 1
while n < 5:
    print(n)
    n = n + 1

n = 1
while n < 5:
    print(n)

num = float(input("Enter a positive number:"))

while num <= 0:
    print("That's not a positive number!")
    num = float(input("Enter a positive number: "))

# The for Loop
for letter in "Phyton":
    print(letter)

word = "Phyton"
index = 0

while index < len(word):
    print(word[index])
    index = index + 1

for n in range(3):
    print("Python")

for n in range(10, 20):
    print(n * n)

amount = float(input("Enter an amount: "))

for num_people in range(2, 6):
    print(f"{num_people} people: ${amount / num_people:,.2f} each")

# Nested Loops

for n in range(1, 4):
    for j in range(4, 7):
        print(f"n - {n} and j - {j}")


# 6.3 - Challenge: Convert temperatures
# Solution to challenge

def convert_cel_to_far(temp_cel):
    """Return the Celsius temperature temp_cel converted to Fahrenheit."""
    temp_far = temp_cel * (9 / 5) + 32
    return temp_far

def convert_far_to_cel(temp_far):
    """Return the Fahrenheit temperature temp_far converted to Celsius."""
    temp_cel = (temp_far - 32) * (5 / 9)
    return temp_cel

# Prompt the user to input a Fahrenheit temperature.
temp_far = input("Enter a temperature in degrees F: ")

# Convert the temperature to Celsius.
# Note that `temp_far` must be converted to a `float`
# since `input()` returns a string.
temp_cel = convert_far_to_cel(float(temp_far))

# Display the converted temperature
print(f"{temp_far} degrees F = {temp_cel:.2f} degrees C")

# You could also use `round()` instead of the formatting mini-language:
# print(f"{temp_far} degrees F = {round(temp_cel, 2)} degrees C"")

# Prompt the user to input a Celsius temperature.
temp_cel = input("\nEnter a temperature in degrees C: ")

# Convert the temperature to Fahrenheit.
temp_far = convert_cel_to_far(float(temp_cel))

# Display the converted temperature
print(f"{temp_cel} degrees C = {temp_far:.2f} degrees F")

# 6.4 - Run in Circles
# Solutions to review exercises

# Exercise 1
# print the integer 2 through 10 using a "for" loop
for i in range(2, 11):
    print(i)

# Exercise 2
# print the integer 2 through 10 using a "while" loop
i = 2
while i < 11:
    print(i)
    i = i + 1

# Exercise 3
def doubles(num):
    """Return the result of multiplying an input number by 2."""
    return num * 2

# Call doubles() to double the number 2 three times
my_num = 2
for i in range(0, 3):
    my_num = doubles(my_num)
    print(my_num)

# 6.5 Challenge: Track Your Investments
def invest(amount, rate, years):

# 6.5 - Challenge: Track Your Investments
# Solution to challenge

# Calculate interest to track the growth of an investment

def invest(amount, rate, years):
    """Display year on year growth of an initial investment"""
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {year}: ${amount:,.2f}")

amount = float(input("Enter a principal amount: "))
rate = float(input("Enter an anual rate of return: "))
years = int(input("Enter a number of years: "))

invest(amount, rate, years)

# 6.6 Understand Scope in Python

x = 2
x

x = 3
x

x = "Hello World"

def func():
    x = 2
    print(f"Inside 'func', x has the value {x}")

func()
print(f"Outside 'func', x has the value {x}")

# Scope Resolution
x = 5
def outer_func():
    y = 3

    def inner_func():
        z = x + y
        return z

    return inner_func()

# Break the Rules
total = 0

def add_to_total(n):
    total = total + n

add_to_total(5)
print(total)

total = 0

def add_to_total(n):
    global total
    total = total + n

add_to_total(5)
print(total)

