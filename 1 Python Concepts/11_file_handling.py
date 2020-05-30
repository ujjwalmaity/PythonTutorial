# WRITE
file = open('demo.txt', 'w')
charNum = file.write('Hello World!\n')
print(charNum)
file.close()

# APPEND
file = open('demo.txt', 'a')
charNum = file.write('UJJWAL')
print(charNum)
file.close()

# READ
file = open('demo.txt', 'r')
content = file.read()
print()
print(content)
file.close()

file = open('demo.txt', 'r')
content = file.read(3)
print()
print(content)
file.close()

file = open('demo.txt', 'r')
content = file.readline()
print()
print(content)
file.close()
