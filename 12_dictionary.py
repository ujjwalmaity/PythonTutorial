people = {"John": 32, "Rob": 23}
print(people)
print(people['John'])

numbers = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
}
print(numbers)
print(1 in numbers)
print(5 in numbers)
print(numbers.get(1))
print(numbers.get(5))
print(numbers.get(5, 'Key not found'))
