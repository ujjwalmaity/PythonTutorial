abc = []

names = ['Mike', 'John', 'Rob']
print(names)
print(names[0])

numbers = [1, 1, 1, 1]
numbers[2] = 5
print(numbers)

newNumbers = [2, 2]
print(numbers + newNumbers)
print(newNumbers * 4)

fruits = ["Apple", "Mango", "Peach"]
print("Mango" in fruits)
print("Orange" in fruits)

# list slicing
numbers = [0, 100, 200, 300, 400, 500, 600]
print(numbers[2:5])
print(numbers[:3])
print(numbers[3:])
print(numbers[1:6:2])

# list comprehension
lis = [x ** 2 for x in range(10)]
print(lis)

lis = [x ** 2 for x in range(10) if x ** 2 % 2 == 0]
print(lis)
