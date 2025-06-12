# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedOrderList = []
        def inorderTraversal(root):
            nonlocal k
            if root is None: return 
            if len(sortedOrderList)==k: return
            inorderTraversal(root.left)
            sortedOrderList.append(root.val)
            inorderTraversal(root.right)
        
        inorderTraversal(root)
        return sortedOrderList[k-1]
