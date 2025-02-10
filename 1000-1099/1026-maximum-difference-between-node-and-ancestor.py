# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, min_val, max_val):
            if root is None:
                return 0

            diff = max(abs(root.val - min_val), abs(root.val - max_val))
            
            new_min = min(min_val, root.val)
            new_max = max(max_val, root.val)

            left = dfs(root.left, new_min, new_max)
            right = dfs(root.right, new_min, new_max)

            return max(diff, left, right)

        return dfs(root, root.val, root.val)
