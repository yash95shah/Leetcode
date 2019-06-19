###Problem 1 - Day 1 - 06/10/2019

'''
Problem 1: Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
Note:
The size of the given array will be in the range [1,1000].
'''


#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    head = None
    current = None

def constructMaximumBinaryTree(self, nums: List[int]) ->:TreeNode:
    m = nums.index(max(nums))
    global head
    global current
    if not head:
        head = TreeNode()
        head.val = max(nums)
        head.left = constructMaximumBinaryTree(self, nums[:m])
        head.right = constructMaximumBinaryTree(self, nums[m + 1:])
    elif not current:
        current = head
    else:
        pass
current.left = constructMaximumBinaryTree(self, nums[:m])
current.right = constructMaximumBinaryTree(self, nums[m + 1:])
return head
'''
