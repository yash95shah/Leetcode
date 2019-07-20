def powerset(arr):
    n = len(arr)
    index = 0
    ans = list()
    temp = set()
    ans.append({})
    while (index < n):

        t_val = arr[index]
        temp.add(t_val)

    return ans


print(powerset([1, 2, 3]))
