myList = [3, "dsd", True, 4]

# Reverse printing of list
for i in range(len(myList)-1, -1, -1):
    print(myList[i])


for i, ele in enumerate(myList):
    print(i, ele)

print()

# While loop
n = 10
while n > 0:
    n -= 1
    if n == 3:
        break
    if n % 2 == 1:
        continue
    print(n)
