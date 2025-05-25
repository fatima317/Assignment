# creates a file and writes content to it
file = open("example.txt", "w")
file.write("Hello, this is a new file.")
file.close()

# read a file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Appends to a file
file = open("example.txt", "a")
file.write("\nAdding another line.")
file.close()

# Reading a file line by line
file = open("example.txt", "r")
for line in file:
    print(line.strip())
file.close()

# with statement (automatic closing of file)
with open("example.txt", "r") as file:
    print(file.read())
