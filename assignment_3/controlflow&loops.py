# Control Flow
# if Statement
age = 12

if age < 18:
    print("You are a minor.") 
#checks if age is less than 18. If true, it runs the print statement. If not, it does nothing.

# elif Statement (with if)
marks = 75

if marks < 50:
    print("Fail")
elif marks < 80:
    print("Pass with average marks") 
#checks if marks are less than 50. If true, it runs the print statement. If not, it checks the next condition.

# else Statement (with if and/or elif)
temperature = 35

if temperature < 20:
    print("It's cold")
elif temperature < 30:
    print("Nice weather")
else:
    print("It's hot")
#checks if temperature is less than 20. If true, it runs the print statement. If not, it checks the next condition. If neither condition is true, it runs the else statement.

#  Nested if Statement 
num = 15

if num > 0:
    print("Number is positive")

    if num % 3 == 0:
        print("It is also divisible by 3") 
    else:
        print("But it's not divisible by 3")

else:
    print("Number is not positive")
#This checks if num is greater than 0. If true, it runs the print statement. Then it checks if num is divisible by 3. If true, it runs the print statement. 
# If not, it runs the else statement. If num is not greater than 0, it runs the else statement.


#LOOPS
#for loop
numbers = [2, 4, 6, 8]

for num in numbers:
    print(f"The square of {num} is {num ** 2}")
#This iterates through each number in the list and prints its square. [4, 16, 36, 64]

word = "hello"

for letter in word:
    print("Letter:", letter)
#This iterates through each letter in the string and prints it. [H, e, l, l, o]

#for Loop with else (No break)
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(f"Checking number: {num}")
else:
    print("Loop completed without a break.")
#iterates through each number in the list and prints it. After the loop, it runs the else statement. 

#for Loop with break (Skipping else)
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(f"Checking number: {num}")
    if num == 3:
        print("Found 3, breaking the loop!")
        break
else:
    print("Loop completed without a break.")
#This iterates through each number in the list and prints it. If it finds 3, it breaks the loop and skips the else statement.

# while loop
count = 0

while count < 5:
    print("Count is:", count)
    count += 1
#simple while loop that increments count by 1 each time until it reaches 5.[0, 1, 2, 3, 4]

# Controlling Loops
# with break
fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
    print("Checking:", fruit)
    if fruit == "mango":
        print("Mango found! Breaking the loop.")
        break
#This iterates through each fruit in the list and prints it. If it finds "mango", it breaks the loop. 

# with continue
for num in range(1, 6):
    if num == 3:
        print("Skipping number 3")
        continue
    print("Number:", num)
#This iterates through numbers 1 to 5. If it finds 3, it skips it and continues with the next number. 

# Nested Loops (loop inside another loop)
list1 = [2, 4]
list2 = [5, 6, 7]

for x in list1:
    for y in list2:
        print(f"{x} x {y} = {x * y}")
#This iterates through each number in list1 and multiplies it with each number in list2. [10, 12, 14, 20, 24, 28]