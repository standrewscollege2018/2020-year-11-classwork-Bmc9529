""" for loop example, for loops run up to but not the final number"""
i = 1
#in for loops we set a start, enging and increment valu
for i in range(0,101):
    if i % 3 and i % 5:
        print("fizzbuzz")
    elif i % 3 and not i % 5:
        print("fizz")
    elif i % 5 and not i % 3:
        print("buzz")
    else:
        print(i)