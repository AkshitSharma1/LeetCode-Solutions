class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        visited = set()
        def bfs(node):
            nonlocal visited
            queue = deque([node])  
            visited.add(node)
            color = defaultdict(lambda:-1)
            color[node] = 0
            n = len(graph)
            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    for neighbour in graph[curr]:
                        #if both the nodes have same color-> not possible case, so we return -1
                        if neighbour in visited and color[neighbour]==color[curr]: return False
                        if neighbour in visited: continue
                        color[neighbour] = (color[curr]+1)%2
                        queue.append(neighbour)
                        visited.add(neighbour)
            return True
        for i in range(len(graph)):
            if i not in visited:
                if bfs(i)==False: return False
        return True