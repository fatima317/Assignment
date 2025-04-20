#**Lists
numbers = [10, 20, 30, 40, 50]
print(numbers)
#creates a list of numbers and prints it.

print(numbers[2])  # Output: 30
print(numbers[-1])  # Output: 50 (last element)
#access elements in the list using positive and negative indexing.

numbers[0] = 5
print(numbers)  # Output: [5, 20, 30, 40, 50]
#modifies the first element of the list.

print(numbers[1:4])  # Output: [20, 30, 40]
#slices the list from index 1 to 3 (4 is not included).

# **list methods
colors = ["red", "green", "blue"]

colors.append("purple")
print(colors)  # Output: ['red', 'yellow', 'blue', 'purple']
#adds "purple" to the end of the list.

colors.extend(["pink", "black"])
print(colors)  
# Output: ['red', 'yellow', 'blue', 'purple', 'pink', 'black']
#adds multiple elements to the end of the list.

colors.remove("blue")
print(colors)  # Output: ['red', 'yellow', 'purple', 'pink', 'black']
#removes "blue" from the list.

colors.pop(1)  # removes 'yellow'
print(colors)  # Output: ['red', 'purple', 'pink', 'black']
#removes the element at index 1.

# **list sorting
numbers = [40, 10, 30, 20]

numbers.sort()
print(numbers)  # Output: [10, 20, 30, 40]
#sorts the list in ascending order.

numbers = [40, 10, 30, 20]
numbers.sort(reverse=True)
print(numbers)  # Output: [40, 30, 20, 10]
#sorts the list in descending order.

words = ["apple", "fig", "banana", "kiwi"]

words.sort(key=len)
print(words)  # Output: ['fig', 'kiwi', 'apple', 'banana']
#sorts the list based on the length of the words.

words.sort(key=lambda word: word[-1])
print(words)   #Output: ['banana', 'apple', 'fig', 'kiwi']
#sorts the list based on the last letter of each word.

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]
#reverses the order of the list.

#**iterating over list
animals = ["cat", "dog", "lion", "tiger"]
for animal in animals:
    print(animal) # Output: cat, dog, lion, tiger
#iterates through each animal in the list and prints it.

# ** tuples
fruits = ("apple", "banana", "cherry")
print(fruits)
# creates a tuple of fruits and prints it.

print(fruits[1])  # Output: banana
#accesses the second element of the tuple.

numbers = (10, 20, 30, 40, 50, 60)
print(numbers[1:4])  # Output: (20, 30, 40)
#slices the tuple from index 1 to 3 (4 is not included).
print(numbers[:3])   # Output: (10, 20, 30)
#slices the tuple from the beginning to index 2 (3 is not included).
print(numbers[3:])  # Output: (40, 50, 60)
#slices the tuple from index 3 to the end.

print(len(fruits))  # Output: 3
#prints the length of the tuple.

colors = ("red", "green")
repeated = colors * 3
print(repeated)  # Output: ('red', 'green', 'red', 'green', 'red', 'green')
#repeats the tuple 3 times.

if "banana" in fruits:
    print("Yes, banana is in the tuple!") # Output: Yes, banana is in the tuple!
#checks if "banana" is in the tuple.

for fruit in fruits:
    print(fruit) # Output: apple, banana, cherry
#iterates through each fruit in the tuple and prints it.

person = "Ali", 25, "Lahore"
name, age, city = person
print(name)  # Output: Ali
print(age)   # Output: 25
print(city)  # Output: Lahore
#unpacks the tuple into variables.

a = (1, 2)
b = (3, 4)
result = a + b
print(result)  # Output: (1, 2, 3, 4)
#concatenates two tuples.

nested = ("apple", ("banana", "cherry"))
print(nested[1][0])  # Output: banana
#accesses the nested tuple and prints "banana".

#** dictionary
person = {
    "name": "Ali",
    "age": 25,
    "city": "Lahore"
}
print(person) 
#creates a dictionary with keys and values and prints it.

print(person["name"])  # Output: Ali
#accesses the value associated with the key "name".
print(person.get("age", "99"))  # Output: 25, if not found it will return 99 (default value)

person["profession"] = "Engineer"
print(person) # Output: {'name': 'Ali', 'age': 25, 'city': 'Lahore', 'profession': 'Engineer'}
#adds a new key-value pair to the dictionary.

person["age"] = 26
print(person)  # Output: {'name': 'Ali', 'age': 26, 'city': 'Lahore', 'profession': 'Engineer'}
#modifies the value associated with the key "age".

del person["city"]
print(person)  # Output: {'name': 'Ali', 'age': 26, 'profession': 'Engineer'}
#deletes the key-value pair with the key "city".

age: int = person.pop("age", -1)
print("Removed age:", age)
print(person) # Output: {'name': 'Ali', 'profession': 'Engineer'}
#removes the key-value pair with the key "age" and returns its value.

for key, value in person.items():
    print(f"{key}: {value}") # Output: name: Ali, profession: Engineer
#iterates through each key-value pair in the dictionary and prints them.


print(person.keys())    # dict_keys(['name', 'age', 'profession'])
print(person.values())  # dict_values(['Ali', 26, 'Engineer'])
print(person.items())   # dict_items([('name', 'Ali'), ('age', 26), ('profession', 'Engineer')])
print(person.update({"name": "Ahmed Ali"})) # {'name': 'Ahmed Ali', 'age': 26, 'profession': 'Engineer'}
print(person.clear()) # {} clears the dictionary.
# dictionary methods

