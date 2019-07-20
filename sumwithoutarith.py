'''

Sum of two integers without actually using the arithmetic operators

'''


def sum_without_arith(num1, num2):
    temp_sum = num1 ^ num2
    and_sum = num1 & num2 << 1
    if and_sum:
        temp_sum = sum_without_arith(temp_sum, and_sum)
    return temp_sum


n1 = int(input("Enter your 1st number: "))
n2 = int(input("Enter your 2nd number: "))

print("Their sum is: " + str(sum_without_arith(n1, n2)))
