# Example-1
def func():
    counter = 0
    while counter < 5:
        yield counter
        counter += 1


for x in func():
    print(x)
print(list(func()))


# Example-2
def even_number(a):
    for i in range(a):
        if i % 2 == 0:
            yield i


print(list(even_number(21)))
