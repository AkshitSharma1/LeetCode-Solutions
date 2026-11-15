# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        def invertNode(root):
            #recursively invert the child nodes first
            if root.left:
                root.left = invertNode(root.left)
            
            if root.right:
                root.right = invertNode(root.right)
            
            root.left,root.right = root.right,root.left
            return root
        
        if root is None: return root
        return invertNode(root)