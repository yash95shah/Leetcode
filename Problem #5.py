import itertools


class Solution:
    def letterCombinations(self, digits: str) :
        mappings = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                    ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        temp_list = []
        res_final = []

        if digits is "":
            return []

        for ch in digits:
            temp_list.append(mappings[int(ch) - 2])
        print (temp_list)
        print ()
        print()
        res = list(itertools.product(*temp_list))
        print (res)
        for each in res:
            elem = ''.join(each)
            res_final.append(elem)

        return res_final


n = Solution()
print (n.letterCombinations("12"))