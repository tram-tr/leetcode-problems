# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res

        frontier = deque([root])
        while frontier:
            level = []
            for _ in range(len(frontier)):
                curr = frontier.popleft()
                level.append(curr.val)
                if curr.left:
                    frontier.append(curr.left)
                if curr.right:
                    frontier.append(curr.right)
            res.append(level)

        return res[::-1]
