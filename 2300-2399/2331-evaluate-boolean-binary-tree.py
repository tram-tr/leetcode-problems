# https://leetcode.com/problems/evaluate-boolean-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        leftEval = self.evaluateTree(root.left)
        rightEval = self.evaluateTree(root.right)

        if root.val == 0 or root.val == 1:
            return root.val == 1
        elif root.val == 2:
            return leftEval or rightEval
        elif root.val == 3:
            return leftEval and rightEval

        return False
