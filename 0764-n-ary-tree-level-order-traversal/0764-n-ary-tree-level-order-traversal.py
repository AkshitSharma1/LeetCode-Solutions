"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def bfs(queue):
            while queue:
                temp = []
                for _ in range(len(queue)):
                
                    node = queue.popleft()
                    if node is None: continue
                    temp.append(node.val)
                    for children in node.children: queue.append(children)
                if len(temp)>0: ans.append(temp.copy())
        queue = deque()
        queue.append(root)
        ans = []
        bfs(queue)
        return ans
            
        