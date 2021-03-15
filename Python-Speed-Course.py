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
