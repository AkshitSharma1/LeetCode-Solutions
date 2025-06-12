"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None: return 0
        maxDepthAns = 0
        for children in root.children:
            maxDepthAns = max(maxDepthAns,self.maxDepth(children))
        return 1 + maxDepthAns
        
        