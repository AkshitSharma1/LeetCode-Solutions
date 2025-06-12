# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answerCount=0
        def dfs(node,maxValue):
            nonlocal answerCount
            if node is None: return
            if node.val>=maxValue:
                answerCount+=1
            
            dfs(node.left,max(maxValue,node.val))
            dfs(node.right,max(maxValue,node.val))
        
        dfs(root,-100000)
        return answerCount

        