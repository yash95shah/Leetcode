def maxsubarray(arr):
    summed = 0
    n = len(arr)
    solution = [0] * n
    for index, val in enumerate(arr):
        print("The index is {} and the value is {} ".format(index, val))
        summed += val
        solution[index] = summed

    return max(solution)


print(maxsubarray([3, 31, -31, 123, 91, 12, -32, -12, -5, 12, 84, 134, -213]))
