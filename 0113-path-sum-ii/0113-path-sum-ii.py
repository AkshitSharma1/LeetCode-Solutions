# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        paths = []
        def dfs(node,curr_sum,curr_path):
            nonlocal paths
            
            #add the current node, see what the sum becomes
            if node is None: return
            curr_sum+=node.val
            curr_path.append(node.val)
           

            if curr_sum==targetSum and  node.left is None and node.right is None :
                #we remove this node and go back
                paths.append(curr_path.copy())
                curr_path.pop() 
                return
            
            dfs(node.left,curr_sum,curr_path)
            dfs(node.right,curr_sum,curr_path)

            curr_path.pop()
        dfs(root,0,[])
        return paths


            
            
