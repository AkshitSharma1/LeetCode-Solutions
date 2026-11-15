# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode | None) -> TreeNode | None:
        def containsOne(root):
            #recursively call child first, true if it contains 1
            if root.left:
                if containsOne(root.left)==False:
                    #left subtree does not contain 1-> we will be removing it
                    root.left = None
                
            if root.right:
                if containsOne(root.right)==False:
                    #right subtree
                    root.right = None
            
            #now if both the branches are gone-> this is a leave node
            # return False-> if it does not contain 1
            if root.left is None and root.right is None and root.val!=1:
                return False
                #above line marks this node for deletion
            
            return True
        if root is None: return None
        if containsOne(root)==False:
            return None
        return root