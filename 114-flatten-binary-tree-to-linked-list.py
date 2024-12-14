# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        curr_node = root

        while curr_node is not None:
            if curr_node.left is not None:
                left_node = curr_node.left
                while left_node.right is not None:
                    left_node = left_node.right
                left_node.right = curr_node.right
                curr_node.right = curr_node.left
                curr_node.left = None
            curr_node = curr_node.right