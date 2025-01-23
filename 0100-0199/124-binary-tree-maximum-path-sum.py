# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        if not root:
            return 0

        def dfs(node): # return max non-split path, including node
            if not node:
                return 0

            left = dfs(node.left) if node.left else 0
            right = dfs(node.right) if node.right else 0

            maxNonSplit = max(node.val, node.val + max(left, right))
            maxSplit = max(node.val, node.val + left + right)

            nonlocal res
            res = max(res, maxNonSplit, maxSplit)

            return maxNonSplit
           
        dfs(root)
        return res
