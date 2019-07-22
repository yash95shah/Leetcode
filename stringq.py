def IsEqualSet(input_string):
    ARRAY_FROM_IPS = list(input_string)
    print(ARRAY_FROM_IPS)
    mid = len(input_string) // 2
    # print (mid)
    # print (mid)
    SET1 = set(ARRAY_FROM_IPS[:mid])
    print(SET1)
    # time.sleep(10)
    SET2 = set(ARRAY_FROM_IPS[mid:])
    print(SET2)
    if SET1 == SET2: return True
    return False


print(IsEqualSet(input_string="abasccabas"))
