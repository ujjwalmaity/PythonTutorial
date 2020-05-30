import re

myString = "My name is John, Hi I'm John."

pattern = r'John'

# Find & Replace
result = re.sub(pattern, 'Rob', myString)

print(result)
