# https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        even = 1
        frontier = deque([root])
        while frontier:
            prev = 0 if even else inf

            for _ in range(len(frontier)):
                curr = frontier.popleft()
                if even and (curr.val % 2 == 0 or prev >= curr.val):
                    return False
                if not even and (curr.val % 2 == 1 or prev <= curr.val):
                    return False
                prev = curr.val

                if curr.left:
                    frontier.append(curr.left)
                if curr.right:
                    frontier.append(curr.right)

            even ^= 1

        return True
