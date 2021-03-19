try:
    x = 7 / 5
except Exception as e:
    print(e)
else:
    print("Nothing went wrong")
finally:
    print('finally')
