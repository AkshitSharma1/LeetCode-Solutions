# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helperFunc(root,lowerBound,upperBound):
            if root is None: return True
            if root.val<=lowerBound or root.val>=upperBound: return False
            if not helperFunc(root.left,lowerBound,root.val): return False
            if not helperFunc(root.right,root.val,upperBound): return False
            return True
        return helperFunc(root,float("-inf"),float("inf"))
        