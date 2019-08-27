from itertools import permutations as ct 
rows = ['r','g','b','r','g','b']
cols =
print (list(ct(rows,3)))



# grid = [['r','g','b'],['b','r','g']]

# #all_rows = list()


# (n)
# def check_if_unique(str):
#     for i in range(len(str)): 
#         for j in range(i + 1,len(str)):  
#             if(str[i] == str[j]): 
#                 return False; 
  
#     # If no duplicate characters  
#     # encountered, return true 
#     return True;
    
# all_rows  = [''.join(row) for row in grid]
# all_cols   = [''.join(col) for col in map(list, zip(*grid))]

# count = 0
# for elem in all_rows:
#     if not check_if_unique(elem):
#         print ("Ok not possible")

# for elem in all_cols:
#     if not check_if_unique(elem):
#         print ("Ok not possible")

        
# print (all_cols)
# '''


# '''

