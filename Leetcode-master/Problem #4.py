import itertools as it


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        for k in it.permutations(nums):
            res.append(k)
        return res
