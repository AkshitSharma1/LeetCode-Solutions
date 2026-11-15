# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        parent = defaultdict(TreeNode)
        parent[root] = None
        def dfs(node):
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)
        dfs(root)
        #we have got the parent array

        def findNode(root,target):
            if root is None: return None
            if root.val==target: return root
            return findNode(root.left,target) or findNode(root.right,target)

        start = findNode(root,start)
        def bfs(start):
            queue = deque([(0,start)]) #distance,node
            visited = set()
            ans = 0
            while queue:
                for _ in range(len(queue)):
                    dist, node = queue.popleft()
                    if node in visited: continue
                    visited.add(node)
                    ans = max(ans,dist)

                    #we process all three- child and parent for this
                    if parent[node] is not None and parent[node] not in visited:
                        queue.append((dist+1,parent[node]))
                    
                    if node.left is not None and node.left not in visited:
                        queue.append((dist+1,node.left))
                    
                    if node.right is not None and node.right not in visited:
                        queue.append((dist+1,node.right))
            return ans
        return bfs(start)