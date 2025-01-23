# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
            
        root = TreeNode(preorder[0])
        rootIdx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:rootIdx + 1], inorder[:rootIdx])
        root.right = self.buildTree(preorder[1 + rootIdx:], inorder[rootIdx + 1:])

        return root
