# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #can this give the max path sum
        maxPathSum = float("-inf")
        def dfs(node):
            nonlocal maxPathSum
            if node is None: return 0
            
            leftMaxSum = dfs(node.left)
            rightMaxSum = dfs(node.right)
          

            maxPathSum= max(maxPathSum,leftMaxSum+rightMaxSum+node.val)

            return max(0,node.val + max(0,max(leftMaxSum,rightMaxSum)))
        dfs(root)
        return maxPathSum

        