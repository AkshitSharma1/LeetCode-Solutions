# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node):
            if node is p or node is q or node is None: return node
            
            left_subtree = lca(node.left)
            right_subtree = lca(node.right)
            if left_subtree and right_subtree:
                return node
            
            return left_subtree or right_subtree
        return lca(root)
