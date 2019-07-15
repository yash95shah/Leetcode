# Recursive Approach

def fib(index):
    temp = {}

    def funct(index):
        if temp.get(index):
            return temp.get(index)
        if (index < 2):
            temp[index] = index
        else:
            temp[index] = funct(index - 1) + funct(index - 2)
        return temp.get(index)

    return funct(index)


print(fib(3))
