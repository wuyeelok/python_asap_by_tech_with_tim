# Dictionary (datatype don't need to be the same)
myDictionary = {'key': 5}
print(myDictionary['key'])

myDictionary['key2'] = 6
myDictionary[9] = [7, 2]
myDictionary[2] = [3, 5, 6, 9]

print(myDictionary)
print()
print(myDictionary.keys())

if 9 in myDictionary:
    print("It has key 9")
