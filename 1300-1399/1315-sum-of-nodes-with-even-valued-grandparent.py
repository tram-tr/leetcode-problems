# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root, subRoot):
            if subRoot is None:
                return

            nonlocal res
            
            if root.val % 2 == 0:
                if subRoot.left:
                    res += subRoot.left.val
                if subRoot.right:
                    res += subRoot.right.val
            dfs(subRoot, subRoot.left)
            dfs(subRoot, subRoot.right)

        dfs(root, root.left)
        dfs(root, root.right)
        
        return res
