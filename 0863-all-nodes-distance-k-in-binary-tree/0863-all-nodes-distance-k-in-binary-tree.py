# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = defaultdict(TreeNode)
        parent[root] = None

        def dfs(node):
            nonlocal parent
            #dfs to get parent array
            if node is None: return
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            
            if node.right:
                parent[node.right] = node
                dfs(node.right)
        

        def bfs(target):
            nonlocal k
            queue = deque([(0,target)])
            visited = set()
            ans = []
            while queue:
                for _ in range(len(queue)):
                    dist, node = queue.popleft() 
                    if node in visited: continue
                    if dist==k: 
                        ans.append(node.val)
                        continue

                    visited.add(node)
                    #process the parent if not done yet

                    if parent[node] is not None and parent[node] not in visited:
                        queue.append((dist+1,parent[node]))

                    #do the same for child nodes
                    if node.left is not None and node.left not in visited:
                        queue.append((dist+1,node.left))

                    if node.right is not None and node.right not in visited:
                        queue.append((dist+1,node.right))
            return ans

        dfs(root)
        return bfs(target)
