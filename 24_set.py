# list : the order of elements is well defined, duplicates are possible
# set : the order of the elements is unknown, elements are unique

numbers = {2, 3, 4, 2, 4, 4, 1}

print(numbers)
print(2 in numbers)

numbers.add(9)
numbers.add(6)
print(numbers)

numbers.remove(6)
print(numbers)
print()

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
print(setA | setB)
print(setA & setB)
print(setA - setB)
