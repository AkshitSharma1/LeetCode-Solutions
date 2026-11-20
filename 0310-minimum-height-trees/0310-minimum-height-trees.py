class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        adj_list = defaultdict(list)
        if len(edges)==0 or n==1: return [0]
        for edge in edges:
            a,b = edge
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        remaining = n #number of remaining nodes
        queue = deque([i for i in range(n) if len(adj_list[i])==1])
        degree = defaultdict(int)
        for i in range(n): degree[i] = len(adj_list[i])
        while queue and remaining>2:
            remaining-=len(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                degree[node]-=1
                
                for neighbour in adj_list[node]:
                    degree[neighbour]-=1
                    if degree[neighbour]==1:
                        queue.append(neighbour)
        return list(queue)
                    


