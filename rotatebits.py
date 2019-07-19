'''
Perform a circular shift of nos


For ex- 0xFFACB >> 8 = 0xBFFAC
Clarify with the interviewer the direction of the shift!
'''


def rotate(x, N):
    return (x >> N | x << (32 - N))


print(hex(rotate(0xFFACB, 8)))
