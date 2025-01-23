# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root or k < 1:
            return 0

        nodes = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)


        dfs(root)
        res = nodes[k - 1]

        return res
