###Problem 2 - Day 2 - 06/12/2019

'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
'''

class Solution:
    def toLowerCase(self, str: str) -> str:
        list_of_str = list(str)
        resultant_str = []
        for x in list_of_str:
            if ord(x) >=97:
                resultant_str.append(x)
            else:
                ch = chr(ord(x) + 96)
                resultant_str.append(ch)
        answer = ''.join(resultant_str)
        return answer


