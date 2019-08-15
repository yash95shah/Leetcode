def exist( matrix , word):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]  == word[0]:
                answer = w_s(word,i,j,matrix)
                if answer == True:
                    return answer
    return False


def w_s(word, i,j,matrix):
    if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]):
        return False 
    elif len(word) == 0:
        return True
    elif matrix[i][j] == word[0]:
        
        return w_s(word[1:],i+1,j, matrix) or w_s(word[1:],i-1,j, matrix) or w_s(word[1:],i,j+1, matrix) or w_s(word[1:],i,j-1, matrix)
    else:
        return False

        


board= [['A','B','C','E'],['S','F','C','S'], ['A','D','E','E']]


word= "BCE"


print (exist(board, word))
