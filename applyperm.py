def apply_perm(Arr, Per):
    if Arr is None or len(Arr) == 0 or len(Arr) != len(Per):
        return 
    for idx , elem in enumerate(Arr):
        if idx == Per[idx]:
            pass
        else:
            Arr = swap_elems(Arr , idx, Per[idx])
            Per = swap_elems(Per, idx, Per[idx] )
    return Arr

        
def swap_elems(any_arr, i,j):
    any_arr[i],any_arr[j] = any_arr[j],any_arr[i]
    return any_arr


Arra  = ['a','b','c','d']    
Permu = [2,0,1,3]
print (apply_perm(Arra,Permu))