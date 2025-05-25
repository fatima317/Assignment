#Types of Modules in Python
# Built-in module
import math
print(math.sqrt(16))

# User-defined module (saved in mymodule.py)
# mymodule.py
def greet(name):
    return f"Hello, {name}"

# Importing user-defined module
import mymodule
print(mymodule.greet("Alice"))

#How to Import a Module in Python
import math  # Import entire module
from math import pi  # Import specific function or variable
import math as m  # Import with alias

print(math.sqrt(25))
print(pi)
print(m.factorial(5))

#Syntax to Define a Python Function
def say_hello():
    print("Hello, world!")

# Function Arguments
def greet(name, age):
    print(f"Hi {name}, you are {age} years old.")

greet("John", 30)

# Keyword Arguments
def describe_pet(animal, name):
    print(f"{name} is a {animal}.")

describe_pet(name="Whiskers", animal="cat")

# Unpacking Iterables
def add(x, y, z):
    print(x + y + z)

nums = [1, 2, 3]
add(*nums)  # Unpacking list

info = {'x': 10, 'y': 20, 'z': 30}
add(**info)  # Unpacking dictionary

# Default Arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Alice")

#Positional-only Arguments
def greet(name, /):
    print(f"Hi {name}")

greet("Alice")  # ✅
# greet(name="Alice")  ❌ Error: 'name' is positional-only

# Keyword-only Arguments
def register(*, username, password):
    print(f"Registered user: {username}")

register(username="john", password="1234")  # ✅
# register("john", "1234")  ❌ Error: must use keywords

# Anonymous Functions (Lambda)
square = lambda x: x * x
print(square(5))

# Keyword Variable-Length Arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")

# Generator Function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)

# Recursive Function 
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Multiple Return Values from Function
def get_info():
    name = "Alice"
    age = 25
    return name, age

n, a = get_info()
print(n, a)
