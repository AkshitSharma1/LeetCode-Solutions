# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        #balanced iff abs height diff <= 1  
        def checkIfBalanced(node):
            if node is None:
                return True,-1
            #function to return true/false and height of this entire tree having root as node
            left_balanced, left_height = checkIfBalanced(node.left)
            right_balanced, right_height = checkIfBalanced(node.right)
            #check if any subtree is unbalanced
            if left_balanced==False or right_balanced==False: return False,-1 
            if abs(right_height-left_height)>1: return False, -1

            return True, 1 + max(left_height,right_height)
        
        is_balanced, max_height = checkIfBalanced(root)
        return is_balanced

