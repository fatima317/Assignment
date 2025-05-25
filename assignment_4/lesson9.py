# Example of a try-except block to handle exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Example of a try-except-else block
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print(f"You entered: {num}")

# Example of a try-except-finally block
try:
    f = open("myfile.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("This block always runs.")

# Example of a try-except-else-finally block 
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Please enter valid numbers.")
else:
    print(f"Result is: {result}")
finally:
    print("Execution finished.")
