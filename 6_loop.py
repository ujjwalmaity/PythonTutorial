# for loop
for x in range(1, 4):
    print(x)

fruits = ["Apple", "Mango", "Peach", "Orange"]
for x in fruits:
    print(x)

for x in range(0, 5, 2):
    print(x)

for num, name in enumerate(fruits):
    print(num, " -> ", name)

# while loop
counter = 0
while counter <= 3:
    print(counter)
    counter += 1
