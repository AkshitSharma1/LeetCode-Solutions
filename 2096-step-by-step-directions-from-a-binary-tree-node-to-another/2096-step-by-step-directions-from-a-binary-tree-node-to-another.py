# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_lca(self,root,val1,val2):
        if root is None or root.val in (val1,val2): return root
        left_part = self.get_lca(root.left,val1,val2)
        right_part = self.get_lca(root.right,val1,val2)
        if left_part and right_part: return root
        return left_part or right_part
    
    def path_to_start(self,root,start_val,path):
        if root is None: return False
        if root.val==start_val: return True
        path.append('U')
        if self.path_to_start(root.left,start_val,path): return True
        path.pop()
        path.append('U')
        if self.path_to_start(root.right,start_val,path): return True
        path.pop()
        return False
    
    def path_to_dest(self,root,dest_val,path):
        if root is None: return False
        if root.val==dest_val: return True
        path.append('L')
        if self.path_to_dest(root.left,dest_val,path): return True
        path.pop()
        path.append('R')
        if self.path_to_dest(root.right,dest_val,path): return True
        path.pop()
        return False
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lca = self.get_lca(root,startValue,destValue)
        path = []
        self.path_to_start(lca,startValue,path)
        self.path_to_dest(lca,destValue,path)
        return "".join(path)