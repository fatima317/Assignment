# **set
my_set = {"apple", "banana", "cherry", "date"}
print(my_set)  # Output order may vary: {'date', 'banana', 'apple', 'cherry'}
# set is unordered, so the output order may vary.
 
# my_set = {["list"]} ❌ TypeError: unhashable type: 'list'
# set cannot contain mutable elements like lists or dictionaries.

my_set.add("fig")
print(my_set) 
my_set.remove("banana")
print(my_set)
#mutable set: adds "fig" and removes "banana".
# set is mutable, so we can add and remove elements.
#but set is unchangeable in the sense that we cannot change an element directly.
# my_set[0] = "grape" ❌ TypeError: 'set' object does not support indexing

my_set.discard("apple")
print(my_set)  # Output: {'date', 'cherry', 'fig'}
# removes "apple" if it exists, but does not raise an error if it doesn't.

my_set.update({"grape", "kiwi"})
print(my_set)  # Output: {'date', 'cherry', 'fig', 'kiwi', 'grape'}
# adds multiple elements to the set.

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Output: {1, 2, 3, 4, 5}
# #union of two sets.

print(a & b)  # Output: {3}
# #intersection of two sets.

print(hash("apple"))   # e.g., 173090321290123901
print(hash(42))        # e.g., 42
#hashing is a way to convert an object into a fixed-size integer.

# **frozen set
numbers = frozenset([1, 2, 3, 4])
print(numbers)
#creates a frozenset (immutable set) and prints it.

# numbers.add(5)     ❌ This will raise an AttributeError
# numbers.remove(2)  ❌ Also not allowed
#attempts to add or remove elements from a frozenset will raise an error.

a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])
print(a.difference(b))  # frozenset({1})
#difference between two frozensets.

print(a.intersection(b))  # frozenset({2, 3})
#intersection of two frozensets.

print(a.union(b))  # frozenset({1, 2, 3, 4})
#union of two frozensets.

print(a.symmetric_difference(b))  # frozenset({1, 4})
#symmetric difference between two frozensets.

print(a.isdisjoint(frozenset([5, 6])))  # True
#checks if two frozensets have no elements in common.
#returns True if they are disjoint.

a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))  # True
print(b.issubset(a))  # False
#checks if one set is a subset of another.
#returns True if the first set is a subset of the second set.

print(b.issuperset(a))  # True
print(a.issuperset(b))  # False
#checks if one set is a superset of another.
#returns True if the first set is a superset of the second set.

original = {10, 20, 30}
copy_set = original.copy()
print(copy_set)  # {10, 20, 30}
print(copy_set is original)  # False (different object)
#creates a new set with the same elements, but it's a different object.

fs = frozenset([1, 2, 3])
fs_copy = fs.copy()
print(fs_copy)  # frozenset({1, 2, 3})
print(fs_copy is fs)  # True — since frozensets are immutable, copy may return same object
#creates a new frozenset with the same elements, but it's a different object.