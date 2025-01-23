# https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            with_curr = node.val + left[1] + right[1]
            without_curr = max(left) + max(right)

            return [with_curr, without_curr]

        return max(dfs(root))
