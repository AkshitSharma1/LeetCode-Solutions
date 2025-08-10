# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        maxSum =0# float('-inf')
        def dfs(node):
            nonlocal maxSum
            if node is None:
                return True,0,float("-inf"),float("inf")
            isLeftBST, leftTreeSum, leftMax,leftMin = dfs(node.left)
            isRightBST,rightTreeSum,rightMax,rightMin = dfs(node.right)

            if isLeftBST and isRightBST and leftMax<node.val<rightMin:
                #This is a BST. 
                currentBSTSum = leftTreeSum+rightTreeSum+node.val
                maxSum = max(currentBSTSum,maxSum)
                maxVal = max(rightMax,node.val)
                minVal = min(leftMin,node.val)
                return True,currentBSTSum,maxVal,minVal
            else:
                return False,-1,-1,-1
        dfs(root)
        return maxSum
        