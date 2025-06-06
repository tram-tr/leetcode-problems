# https://leetcode.com/problems/inorder-successor-in-bst/

'''
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.


The successor of a node p is the node with the smallest key greater than p.val.


Example:
        5
     3     6
  2     4
1


p = 1 => output 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.


Constraints:
The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
All Nodes will have unique values.
'''

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None

        res = None
        while root:
            if root.val > p.val:
                res = root
                root = root.left
            else:
                root = root.right

        return res
