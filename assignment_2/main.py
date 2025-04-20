#1. Arithmetic Operators
a = 15
b = 4

print(a + b)   # Addition: 19
print(a - b)   # Subtraction: 11
print(a * b)   # Multiplication: 60
print(a / b)   # Division: 3.75
print(a % b)   # Modulus: 3
print(a ** b)  # Exponentiation: 50625
print(a // b)  # Floor division: 3

#2. Assignment Operators
x = 20
x += 5
print(x)  # 25

x -= 10
print(x)  # 15

x *= 3
print(x)  # 45

x /= 5
print(x)  # 9.0

x %= 4
print(x)  # 1.0

# 3. Comparison Operators
a = 7
b = 12

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True

# 4. Logical Operators
x = False
y = True

print(x and y)  # False
print(x or y)   # True
print(not y)    # False

# 5. Identity Operators
a = [4, 5, 6]
b = a
c = [4, 5, 6]

print(a is b)      # True
print(a is c)      # False
print(b is not c)  # True

# 6. Membership Operators
colors = ["red", "green", "blue"]

print("green" in colors)       # True
print("yellow" not in colors)  # True

# 7. Bitwise Operators
a = 6     # 0110
b = 2     # 0010

print(a & b)   # 2  (0010)
print(a | b)   # 6  (0110)
print(a ^ b)   # 4  (0100)
print(~a)      # -7 (bitwise NOT)
print(a << 1)  # 12 (shift left)
print(a >> 1)  # 3  (shift right)
