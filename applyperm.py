def apply_perm(Arr, Per):
    if Arr is None or len(Arr) == 0 or len(Arr) != len(Per):
        return 
    for idx in range(len(Arr)):
        if idx == Per[idx]:
            pass
        else:
            Arr = swap_elems(Arr , idx, Per[idx])
            Per = swap_elems(Per, idx, Per[idx] )
    return Arr


def bad_sol(Arr, Perm):
    ext_arr = [0]*len(Arr)
    for idx, val in enumerate(Perm):
        ext_arr[val] = Arr[idx]
    return ext_arr

        
def swap_elems(any_arr, i,j):
    any_arr[i],any_arr[j] = any_arr[j],any_arr[i]
    return any_arr


Arra  = ['a','b','c','d','e','f']    
Permu = [1,0,5,4,3,2]
# b a f e d c
print (bad_sol(Arra,Permu))