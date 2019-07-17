# Count the no of ones in  a binary no

def coutones(num):
    sum = 0
    while (num > 0):
        sum += num & 1
        num >>= 1
    return sum


print(coutones(num=8))
