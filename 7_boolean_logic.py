username = 'admin'
password = 'admin123'

if username == 'admin' and password == 'admin123':
    print('Valid User')
else:
    print('Invalid User')

if username == 'admin' or password == '':
    print('Valid User')
else:
    print('Invalid User')

# False -> 0, '', [], None
if not '':
    print('True')
else:
    print('False')
