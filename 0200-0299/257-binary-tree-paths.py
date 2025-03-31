# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         res = []

#         def dfs(root, s):
#             if not root:
#                 return

#             if not root.left and not root.right:
#                 res.append(s + str(root.val))
            
#             s += str(root.val)
#             if root.left:
#                 dfs(root.left, s + "->")
#             if root.right:
#                 dfs(root.right, s + "->")

#         dfs(root, "")

#         return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def backtracking(node, path):
            if not node:
                return

            # add this node’s value to the path
            path.append(node.val)

            # if it's a leaf, record the path
            if not node.left and not node.right:
                res.append("->".join(str(val) for val in path))

            # otherwise
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)

            # backtrack – remove the last node added
            path.pop()

        backtracking(root, [])
        return res

            
