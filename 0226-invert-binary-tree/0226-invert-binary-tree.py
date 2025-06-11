# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Base case
        if root is None: return None
        #Invert left tree
        leftChild = self.invertTree(root.left)
        
        #Invert right tree
        rightChild = self.invertTree(root.right)

        #Now, invert these two child values
        
        root.left,root.right = rightChild,leftChild
        
        return root

        