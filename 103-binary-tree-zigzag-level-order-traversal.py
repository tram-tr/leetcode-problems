# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        traversal = []
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        level_idx = 0

        while len(queue) > 0:
            curr_level = []
            num_nodes = len(queue)
            for _ in range(num_nodes):
                curr_node = queue.popleft()

                if level_idx % 2 == 0:
                    curr_level.append(curr_node.val)
                else:
                    curr_level.insert(0, curr_node.val)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            level_idx += 1
            traversal.append(curr_level)

        return traversal