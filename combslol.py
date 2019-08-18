from itertools import product

a = [['A','B','C'],['D'],['E','F','G']]




def print_combs(arr):
    for elem in arr:
        print (elem)
    
    return list(product(*arr))



print (print_combs(a))


def prods (*args):
    