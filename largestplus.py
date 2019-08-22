




# # def largestPlus(N:int, mines:List[List[int]])->int:
#     pass
order = 1
mines = [[4,2],[1,2],[2,1],[2,3]]
matrix =[ [1] * 5  for _ in range(5)] 

def maxorderplus(matrix, mines):
    temp, final = 0,0
    for x in mines:
        matrix[x[0]][x[1]] = 0
    print (matrix)
    for x in range(5):
        for y in range(5):
            if matrix[x][y] == 1:
                temp = giveorder(x,y, matrix)
                if temp > final:
                    final =  temp
    return final

def giveorder(i, j, matrix):
    order = 1

    while i+order <= 4 and i-order >= 0 and j+order <= 4 and j -order >= 0 and matrix[i+order][j] == 1 and matrix[i-order][j] == 1 and matrix[i][j+order] == 1 and matrix[i][j-order] == 1:
        print (str(i)+" " +str(j))
        
        order += 1
    return order

    #matrix[2] = [8] * 5
'''
1 1 1 1 1
1 1 0 1 1
1 0 1 0 1
1 1 1 1 1
1 1 0 1 1

'''



print (maxorderplus(matrix, mines))