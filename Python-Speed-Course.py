x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z < x+2

print(result1 and result2)
print(result1 or result2)
print(not result3)
print(result3 or not result2 or result1)

# for detail of operator precedence in Python see
# https://docs.python.org/3/reference/expressions.html#operator-precedence
