# Python - List Comprehension
myList = [item for item in range(10)]
print("myList: {}".format(myList))


# Python - normal for loop
myList2 = []
for item in range(10):
    myList2.append(item)
print("myList2: {}".format(myList2))


# List Comprehesion can also turn string into list
myNameList = [letter for letter in 'Kenneth']
print("myNameList is {}".format(myNameList))


x = [[x for x in range(4)] for x in range(5)]
print(x)

y = tuple(i for i in range(100) if i % 5 == 0)
print(y)
