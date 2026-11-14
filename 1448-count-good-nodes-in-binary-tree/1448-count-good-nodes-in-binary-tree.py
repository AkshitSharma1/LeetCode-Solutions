# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #logic-> go across all the nodes, capturing max value along the path and see if it does not exist the final node value or not
        good_nodes_count = 0

        def dfs(node,max_value):
            if node is None: return

            nonlocal good_nodes_count
            #to write basecase

            if node.val>=max_value:
                good_nodes_count +=1
                max_value = node.val
            
            dfs(node.left,max_value)
            dfs(node.right,max_value)
        
        dfs(root,float("-inf"))
        return good_nodes_count

        