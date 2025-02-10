# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res

        frontier = deque([root])
        max_s = -inf
        level = 0

        while frontier:
            level += 1
            s = 0
            for _ in range(len(frontier)):
                curr = frontier.popleft()
                s += curr.val
                if curr.left:
                    frontier.append(curr.left)
                if curr.right:
                    frontier.append(curr.right)
            if max_s < s:
                max_s = s
                res = level
                
        return res
