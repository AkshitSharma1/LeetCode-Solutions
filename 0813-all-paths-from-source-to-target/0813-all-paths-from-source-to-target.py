from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adjList = graph
        allPaths=[]
        pq = deque()
        pq.append((0,[0]))
        n = len(graph)
        visited = set()
        while pq:
            node,path = pq.popleft()
        
            if len(path)!=0 and path[-1]==n-1:
                allPaths.append(path)
                continue
            
            for neighbour in adjList[node]:
                pq.append((neighbour,path+[neighbour]))
        return allPaths

        