# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def dfs(node):
            nonlocal answer
            if node is None: return -1
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            answer = max(answer,2+left_height+right_height)
            return 1 + max(left_height,right_height)
        dfs(root)
        return answer
