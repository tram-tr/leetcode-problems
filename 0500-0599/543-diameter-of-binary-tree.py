# https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left) 
            right = dfs(node.right) 

            maxNonSplit = max(1, 1 + max(left, right))
            maxSplit = max(1, 1 + left + right)

            nonlocal res
            res = max(res, maxNonSplit, maxSplit)

            return maxNonSplit

        dfs(root)

        return res - 1
