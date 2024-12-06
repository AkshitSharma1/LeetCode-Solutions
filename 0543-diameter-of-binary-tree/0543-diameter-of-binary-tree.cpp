/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int ans=0;
    int diameterOfBinaryTree2(TreeNode* root) {
        if (root==NULL) return 0;
        int leftHeight = diameterOfBinaryTree2(root->left);
        int rightHeight = diameterOfBinaryTree2(root->right);
        ans = max(ans,leftHeight+rightHeight);
        return 1 + max(leftHeight,rightHeight);

    }

      int diameterOfBinaryTree(TreeNode* root) {
         diameterOfBinaryTree2(root);
         return ans;

    }
};