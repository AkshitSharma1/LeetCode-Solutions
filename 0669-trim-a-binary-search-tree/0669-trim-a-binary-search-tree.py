# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode | None, low: int, high: int) -> TreeNode | None:
        def preorder(root):
            nonlocal low,high
            if root is None:
                return
            
            if root.val<low:
                return preorder(root.right)
            if root.val>high:
                return preorder(root.left)
            

            
            root.left = preorder(root.left)
            root.right = preorder(root.right)
            return root
        return preorder(root)
        

            
