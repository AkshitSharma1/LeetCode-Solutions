# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = float("-inf")
        # base case- when only 1 node
    
        def max_path_sum(node):
            nonlocal answer
            if node is None: return 0
            left_path_sum = max_path_sum(node.left)
            right_path_sum = max_path_sum(node.right)
            answer = max(answer,
            max(0,left_path_sum)+max(0,right_path_sum)+node.val)
            value_to_return = node.val + max(0,max(left_path_sum,right_path_sum))
            
            return value_to_return
        max_path_sum(root)
        return answer


        