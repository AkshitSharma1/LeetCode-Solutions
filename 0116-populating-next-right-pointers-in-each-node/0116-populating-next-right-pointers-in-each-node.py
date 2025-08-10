"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return None
        queue = deque()
        queue.append(root)
        answer = []
        def bfs(queue):
            
            while queue:
                lastNode = None
                for _ in range(len(queue)):
                    currNode = queue.popleft()
                    currNode.next = lastNode
                    lastNode = currNode
                    if currNode.right is not None: queue.append(currNode.right)
                    if currNode.left is not None: queue.append(currNode.left)
        bfs(queue)
        return root

