def twomissing(input_array):
    set_from_input = list()
    max_from_array = max(input_array)
    print(max_from_array)
    if len(input_array) <= max_from_array:
        for i in range(max_from_array):
            # print (i)
            if i + 1 not in input_array:
                set_from_input.append(i + 1)
        if len(set_from_input) == 1: set_from_input.append(max_from_array + 1)
    else:
        return "Error"
    return set_from_input


print(twomissing([1, 2, 4]))
