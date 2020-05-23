# Simple function
def func():
    print('Function called.')


func()


# Passing argument to function
def sub(a, b):
    print(a - b)


sub(3, 1)


# Making function return value
def add(a, b):
    return a + b


print(add(3, 1))


# Passing function as argument
def square(x):
    return x * x


print(square(add(2, 3)))
