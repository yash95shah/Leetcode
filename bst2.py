'''
Treasure Island--

You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in.
There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.
Assume the map area is a two dimensional grid, represented by a matrix of characters.
You must start from the top-left corner of the map and can move one block up, down, left or right at a time.
The treasure island is marked as ‘X’ in a block of the matrix. ‘X’ will not be at the top-left corner.
Any block with dangerous rocks or reefs will be marked as ‘D’. You must not enter dangerous blocks. You cannot leave the map area.
Other areas ‘O’ are safe to sail in. The top-left corner is always safe.
Output the minimum number of steps to get to the treasure.
e.g.
Input
[
[‘O’, ‘O’, ‘O’, ‘O’],
[‘D’, ‘O’, ‘D’, ‘O’],
[‘O’, ‘O’, ‘O’, ‘O’],
[‘X’, ‘D’, ‘D’, ‘O’],
]

Output from aonecode.com
Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.

'''


def find_location_of_target(grid):
    if not grid: return
    n = len(grid[0])
    for i_row in range(n):
        for j_col in range(n):
            if grid[i_row][j_col] == 'X':
                return i_row, j_col


def main_function(grid):
    start_pos_row = 0
    start_pos_col = 0
    end_pos_row, end_pos_col = find_location_of_target(grid)
    temp = list()
    bool = list()

    def helper_function(row_target, col_target, temp, bool):
        if bool[row_target, col_target] == False: return
        if row_target < 0 or col_target < 0 or row_target >= n or col_target >= n: return 0
        if row_target == start_pos_row and col_target == start_pos_col: return 1
        if grid[row_target, col_target] == 'D': return 10000
        bool[row_target, col_target] = False
        if temp[row_target, col_target]:
            return temp
        else:
            temp[row_target, col_target] = min(helper_function(row_target - 1, col_target, temp),
                                               helper_function(row_target, col_target + 1, temp),
                                               helper_function(row_target + 1, col_target, temp),
                                               helper_function(row_target, col_target - 1, temp)

            retun
            temp

            '''
            
            '''
