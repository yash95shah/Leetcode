def maxorderplus(N, mines):
    if len(mines)==N**2: return 0
    grid = [['1']*N for _ in range(N)]
    for i,j in mines: grid[i][j]='0'
    grid_row = [''.join(row) for row in grid]
    grid_col = [''.join(col) for col in map(list, zip(*grid))]
    res = 1
    for i in range(N):
        for j in range(N):
            if grid[i][j]=='1':
                while True:
                    if (j-res>=0 and j+res<N and i-res>=0 and i+res<N and
                        '0' not in grid_row[i][j-res:j+res+1] and
                        '0' not in grid_col[j][i-res:i+res+1]):
                        res+=1                                     
                    else:  
                        break
    return res



mines = [[4,2]]

print (maxorderplus(5, mines))