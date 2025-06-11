# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None: return -1
            leftChild = height(node.left)
            rightChild = height(node.right)
            if leftChild==-2 or rightChild==-2: return -2
            if abs(leftChild-rightChild)>1: return -2

            
            return 1+max(leftChild,rightChild)

        answer = height(root)
        if answer==-2: return False
        return True
        