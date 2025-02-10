# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res

        frontier = deque([root])

        while frontier:
            level = []

            for _ in range(len(frontier)):
                curr = frontier.popleft()
                level.append(curr.val)
                frontier.extend(curr.children)

            res.append(level)

        return res
