def powerset(arr):
    n = len(arr)
    index = 0
    ans = list()
    temp = set()
    ans.append({})
    while (index < n):
        t_val = arr[index]
        temp.add(t_val)
        ans.append(temp)
        index += 1
        print(ans)


print(powerset([1, 2, 3]))
