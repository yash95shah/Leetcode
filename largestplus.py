




# # def largestPlus(N:int, mines:List[List[int]])->int:
#     pass
order = 1
mines = []
matrix =[ [1] * 2  for _ in range(2)] 

def maxorderplus(matrix, mines):
    temp, final = 0,0
    for x in mines:
        matrix[x[0]][x[1]] = 0
    for x in range(5):
        for y in range(5):
            temp = giveorder(x,y, matrix)
            if temp > final:
                final =  temp
    return final

def giveorder(i, j, matrix):
    order = 1
    if i+order > 1 or i-order < 0 or j+order > 1 or j -order < 0:
        return order
    while i+order <= 1 and i-order >= 0 and j+order <= 1 and j -order >= 0 and matrix[i+order][j] == 1 and matrix[i-order][j] == 1 and matrix[i][j+order] == 1 and matrix[i][j-order] == 1:
        order += 1
    return order

    #matrix[2] = [8] * 5
'''
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 0 1 1

'''


print (matrix)
print (maxorderplus(matrix, mines))