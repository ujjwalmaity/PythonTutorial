def add(x):
    return x + 2


myList = [10, 20, 30, 40]

newList = list(map(add, myList))
print(newList)

newList = list(map(lambda x: x * 2, myList))
print(newList)
