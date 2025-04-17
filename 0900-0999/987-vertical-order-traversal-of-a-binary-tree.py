# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(list)
        q = deque()
        q.append((root,0,0))

        while q:
            for _ in range(len(q)):
                node, row_idx, col_idx = q.pop()
                nodes[col_idx].append((row_idx,node.val))
                if node.left:
                    q.append((node.left, row_idx+1, col_idx-1))
                if node.right:
                    q.append([node.right, row_idx+1, col_idx+1])

        res = []
        for col in sorted(nodes.keys()):
            res.append([val for _, val in sorted(nodes[col])])

        return res
