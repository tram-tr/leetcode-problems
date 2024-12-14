/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // Time: best - O(logN) (when the BST is balanced); worst - O(N)
        // Space: O(1)
        int left = min(p->val, q->val);
        int right = max(p->val, q->val);

        while (root != nullptr) {
            if (root->val < left)
                root = root->right;
            else if (root->val > right)
                root = root->left;
            else
                return root;
        }

        return nullptr;
    }
};
