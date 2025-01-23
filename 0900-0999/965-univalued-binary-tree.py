# https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftEval = self.isUnivalTree(root.left)
        rightEval = self.isUnivalTree(root.right)

        if not leftEval or not rightEval:
            return False

        if root.left and root.val != root.left.val:
            return False
        if root.right and root.val != root.right.val:
            return False

        return True
