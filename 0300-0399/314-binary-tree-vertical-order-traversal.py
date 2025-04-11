# https://leetcode.com/problems/binary-tree-vertical-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       cols = {}
       def dfs(node, row, col):
           nonlocal cols
           if node is None:
               return


           if col not in cols:
               cols[col] = []
          
           cols[col].append((row, node.val))
           dfs(node.left, row+1, col-1)
           dfs(node.right, row+1, col+1)


       dfs(root, 0, 0)
       res = []
       for col in sorted(cols.keys()):
           res.append([val for a, val in sorted(cols[col], key=lambda x: x[0])])


       return res
