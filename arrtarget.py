#! usr/bin/env python
arr = [1, 4, 2, 5, 7, 4]
target = 5


def return_pair(array, target_sum):
    set_from_array = set(array)
    for i in set_from_array:
        temp_required_value = target_sum - i
        if temp_required_value in set_from_array:
            u = array.index(i)
            v = array.index(temp_required_value)
            return (u, v)
    return False


print(return_pair(array=arr, target_sum=target))
