# Write a method to return all subsets of a set.
from itertools import chain, combinations


# result = set()

def subsets(set):
   s = list(set)
   return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


# print (list(subsets({1,2,3,4})))

# def powerset(s):
#    x = len(s)
#    masks = [1 << i for i in range(x)]
#
# for i in range(1 << x):
#    yield [ss for mask, ss in zip(masks, s) if i & mask]


print(list(subsets({1, 2, 3, 4})))
