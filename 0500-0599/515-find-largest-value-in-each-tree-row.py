# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        frontier = deque([root])

        while frontier:
            max_val = -inf
            for _ in range(len(frontier)):
                curr = frontier.popleft()
                max_val = max(max_val, curr.val)
                if curr.left:
                    frontier.append(curr.left)
                if curr.right:
                    frontier.append(curr.right)
            res.append(max_val)

        return res
