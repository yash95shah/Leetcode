'''

know swapping works on python without actually using temps
'''


def swap(x, y):
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return (x, y)


x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

print("New value of x and y:    " + str(swap(x, y)))
