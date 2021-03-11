# empty set
x = set()
print(type(x))

# empty dictionary
y = {}
print(type(y))

# Init set, watch out the diff with dictionary
z = {2, 4, "sdf", 4}
print(type(z))
print(z)
print('asfweef' in z)

if("sdf" in z):
    print("the element sdf in in Set z")
