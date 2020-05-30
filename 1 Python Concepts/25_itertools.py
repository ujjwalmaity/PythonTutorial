from itertools import count, accumulate, takewhile

numbers = []
for i in count(3):
    numbers.append(i)
    if i >= 20:
        break
print(numbers)

numbers = list(accumulate(range(10)))
print(numbers)

numbers = list(takewhile(lambda x: x <= 10, numbers))
print(numbers)
