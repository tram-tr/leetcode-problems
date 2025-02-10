# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if not root:
            return res

        frontier = deque([root])
        
        while frontier:
            s = 0
            n = len(frontier)
            for _ in range(n):
                curr = frontier.popleft()
                s += curr.val
                if curr.left:
                    frontier.append(curr.left)
                if curr.right:
                    frontier.append(curr.right)
            res.append(s / n)

        return res
