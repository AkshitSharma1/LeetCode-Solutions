# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        p_pointer = p
        q_pointer = q
        def dfs(p,q):
            # to write basecases
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False

            if p.val==q.val and dfs(p.left,q.left) and dfs(p.right,q.right): 
                return True
            #all ther cases-> return false
            return False
        return dfs(p,q)
        