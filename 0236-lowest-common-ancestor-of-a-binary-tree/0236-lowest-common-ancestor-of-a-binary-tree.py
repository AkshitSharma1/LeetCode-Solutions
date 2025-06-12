# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or root in (p,q):
            return root
        
        leftSubtree = self.lowestCommonAncestor(root.left,p,q)
        rightSubtree = self.lowestCommonAncestor(root.right,p,q)
        
        return root if (leftSubtree and rightSubtree) else (leftSubtree or rightSubtree)
