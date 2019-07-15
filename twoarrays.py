#! /usr/bin/env python


arr1 = [4, 5, 1, 2]
arr2 = [1, 4, 6, 3]
HARD_NUM = 10


def closest_num(arr1, arr2, hardno):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    dev = abs(arr1[0] + arr2[0] - hardno)

    def helper(arr1, arr2, hardno, dev):
        n = len(arr2)
        m = len(arr1)
        t_dev = (arr1[0] + arr2[n - 1] - hardno)
        if (abs(t_dev) < dev):
            new_pair = (arr1[0], arr2[n - 1])
            dev = abs(t_dev)
        if t_dev < 0:
            v = arr1[0]
            arr1.remove(v)
        elif t_dev == 0:
            return (arr1[0], arr2[n - 1])
        else:
            u = arr2[n - 1]
        if len(arr1) == 1 or len(arr2) == 1:
            return new_pair
        else:
            helper(arr1, arr2, hardno, dev)

    return helper(arr1, arr2, hardno, dev)


print(closest_num(arr1, arr2, HARD_NUM))
