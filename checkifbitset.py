def is_nth_bit_set(number, n):
    if n == 1 and number & 1:
        return True
    elif n == 1 and number & 1:
        return False
    while number > 0 and n > 1:
        number >>= 1
        n -= 1
        if number <= 0:
            return Exception("You can't select this bit cause it doesn't exist")
    if number & 1:
        return True
    return False


print(is_nth_bit_set(12, 4))

# 1 1 0 0
