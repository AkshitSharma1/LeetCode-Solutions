# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        def dfs(root):
            nonlocal heap
            if root is None: return
            heapq.heappush(heap,root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        for _ in range(k-1):
            heapq.heappop(heap)
        return heapq.heappop(heap)
