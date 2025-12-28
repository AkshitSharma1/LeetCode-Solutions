# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = defaultdict(lambda:-1)
        def recursive_sol(node):
            if node is None: return 0
            if dp[node]!=-1: return dp[node]
            dp[node] = max(node.val+
            (recursive_sol(node.left.left) + recursive_sol(node.left.right) if node.left is not None else 0)+
            (recursive_sol(node.right.left) + recursive_sol(node.right.right) if node.right is not None else 0),
            0 + recursive_sol(node.left)+recursive_sol(node.right))
            return dp[node]
        return recursive_sol(root)
            

        