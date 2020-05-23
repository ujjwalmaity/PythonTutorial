def div(a, b):
    print(a / b)


try:
    div(2, 0)
except ZeroDivisionError:
    print('There is divide by zero error.')
except Exception as e:
    print(e)
finally:
    print('Finally called.')
