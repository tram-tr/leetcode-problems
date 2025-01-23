# https://leetcode.com/problems/range-sum-of-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        if low <= root.val <= high:
            left = self.rangeSumBST(root.left, low, high)
            right = self.rangeSumBST(root.right, low, high)
            return root.val + left + right
        
        elif root.val < low:
            right = self.rangeSumBST(root.right, low, high)
            return right

        else:
            left = self.rangeSumBST(root.left, low, high)
            return left
