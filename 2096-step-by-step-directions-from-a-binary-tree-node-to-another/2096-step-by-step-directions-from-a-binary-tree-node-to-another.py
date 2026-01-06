# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_lca(self,curr_node,val1,val2):
        if  curr_node is None  or curr_node.val==val1 or curr_node.val== val2:
            return curr_node
        left_side = self.get_lca(curr_node.left,val1,val2)
        right_side = self.get_lca(curr_node.right,val1,val2)
        if left_side and right_side: return curr_node
        return left_side or right_side
    
    def backtrack_path_startnode(self,curr_node,target_val,path):
        if curr_node==None: return False
        if curr_node.val==target_val:
            return True
        path.append('U')    
        try_left = self.backtrack_path_startnode(curr_node.left,target_val,path)
        if try_left: return True
        try_right = self.backtrack_path_startnode(curr_node.right,target_val,path)
        if try_right: return True
        path.pop()
        return False
    
    def backtrack_path_endnode(self,curr_node,target_val,path):
        if curr_node==None: return False
        if curr_node.val==target_val:
            return True
        path.append('L')    
        try_left = self.backtrack_path_endnode(curr_node.left,target_val,path)
        if try_left: return True
        path.pop()
        path.append('R')    
        try_right = self.backtrack_path_endnode(curr_node.right,target_val,path)
        if try_right: return True
        path.pop()
        return False

        
        
    


        

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lca = self.get_lca(root,startValue,destValue)
        path_to_start = []
        path_to_dest = []
        self.backtrack_path_startnode(lca,startValue,path_to_start)
        self.backtrack_path_endnode(lca,destValue,path_to_start)
        return "".join(path_to_start+path_to_dest)

        

        
        