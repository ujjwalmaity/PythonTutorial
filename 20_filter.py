myList = [1, 3, 4, 5, 7, 2, 9, 11, 13]

newList = list(filter(lambda x: x % 2 == 0, myList))

print(newList)
