# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        frontier = deque([root])

        while frontier:
            s = 0
            for _ in range(len(frontier)):
                curr = frontier.popleft()
                s += curr.val
                if curr.left:
                    frontier.append(curr.left)
                if curr.right:
                    frontier.append(curr.right)

        return s
