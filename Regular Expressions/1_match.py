import re

# r -> raw string
pattern = r'eggs'

if re.match(pattern, 'eggseggseggs'):
    print('Match Found')

if re.match(pattern, 'eggseggsabc'):
    print('Match Found')

if re.match(pattern, 'abceggseggseggs'):
    print('Match Found')
else:
    print('No Match Found')
