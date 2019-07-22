def threesum(arr):
    arr.sort()
    temp = set()

    for i in range(len(arr) - 3):
        if i == 0 or arr[i] > arr[i + 1]:
            start = i + 1
            end = len(arr) - 1
            while (start < end):
                if arr[start] + arr[end] + arr[i] == 0:
                    temp.add(arr[i])
                    temp.add(arr[start])
                    temp.add(arr[end])
                if arr[start] + arr[end] + arr[i] < 0:
                    cur = start
                    #    while arr[cur] == arr[start] and start < end:
                    start += 1
                else:
                    cur = end
                    #   while arr[cur] == arr[end] and start < end:
                    end -= 1
    return temp


print(threesum([-1, -4, 2, 5, 6, 3, 7, 23, 21]))
