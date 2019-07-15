# import math
# def main():
#     print ("Hello fuckers")
#
# class Solver:
#     def demo(self, a, b, c):
#         d = b ** 2 - 4 * a * c
#         if d > 0:
#             disc = math.sqrt(d)
#             root1 = (-b + disc) / (2 * a)
#             root2 = (-b - disc) / (2 * a)
#             print("Hallelujah")
#             print("root1 has been found" + root1)
#             return root1, root2
#         elif d == 0:
#             return -b / (2 * a)
#         else:
#             return "This equation has no roots"
#
# class random():
#     def __init__ (self, minutes):
#         self.mins = minutes
#     def __str__(self):
#         return str(self.mins/60)
#
# if __name__ == '__main__':
#     main()
#     m   = random(120)
#     hours = str(m)
#
#     print (hours)
#
#
#


# t a c o c a t

def is_palindrome_perm(input_string):
    input_string = input_string.replace(" ", "")
    input_string = input_string.lower()

    d = {}

    for i in input_string:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    # def make_pali_w(input_string, d):
    #     resultant_string = str()
    #     if len(input_string) % 2 != 0:
    #

    odd_occ = 0
    for k, v in d.items():
        if v % 2 != 0 and odd_occ == 0:
            odd_occ += 1
        elif v % 2 != 0 and odd_occ != 0:
            return False
    return True


print(is_palindrome_perm("aabbcc"))
# c a b b a c
