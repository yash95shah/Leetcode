# Write a method to return all subsets of a set.
#
from itertools import chain, combinations

#result = set()

def subsets(set):
   s = list(set)
   return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))


print (list(subsets({1,2,3,4})))