names = []
for a in range(5):
    name = input("List name: ")
    names.append(name)
length = len(names)
i = 0

while i < length:
    print(names[i] + " is awesome!")
    i += 1