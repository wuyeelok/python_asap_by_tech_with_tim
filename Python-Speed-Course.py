myList = [4, 6, 23, 34, 434, 2344, 24453, 1]

myNewList = list(map(lambda i: i+2, myList))

myNewList2 = list(filter(lambda i: i % 2 == 0, myList))

print(myList)
print()
print(myNewList)
print()
print(myNewList2)
