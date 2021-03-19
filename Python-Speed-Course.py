# mutiply args
def my_mutiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


print(my_mutiply(4, 2, 5))

# Use start when calling and passing mutiple argument


def myFunc(x, y):
    print(x, y)


pairs = [(1, 2), (3, 4)]

for pair in pairs:
    myFunc(*pair)


def yourFunc(*args, **kwargs):
    print(args, kwargs)


yourFunc(4, 2, 1, one=0, tow=1)
