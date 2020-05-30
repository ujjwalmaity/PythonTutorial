import re

pattern = r'eggs'

if re.search(pattern, 'abceggseggseggsabc'):
    print('Match Found')

print(re.findall(pattern, 'abceggseggseggsabc'))
