# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        frontier = deque()
        frontier.append(root)

        while frontier:
            prev = None
            for _ in range(len(frontier)):
                node = frontier.popleft()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    frontier.append(node.left)
                if node.right:
                    frontier.append(node.right)
        
        return root
