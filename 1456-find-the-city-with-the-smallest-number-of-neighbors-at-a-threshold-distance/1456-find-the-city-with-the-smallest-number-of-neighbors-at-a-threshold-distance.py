from collections import defaultdict
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjList = defaultdict(list)
        m = len(edges)
        dist = [[1e7 for _ in range(n)] for _ in range(n)]
        for i in range(n): dist[i][i]=0
        for edge in edges:
            adjList[edge[0]].append((edge[1],edge[2]))
            adjList[edge[1]].append((edge[0],edge[2]))
            dist[edge[1]][edge[0]]=edge[2]
            dist[edge[0]][edge[1]]=edge[2]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
                    dist[j][i]=dist[i][j]
        smallestCity=0
        smallestCityCount=1e7

        for i in range(n):
            temp=0
            for neighbour,distance in enumerate(dist[i]):
                if neighbour!=i and distance<=distanceThreshold: temp+=1
            if temp<=smallestCityCount:
                smallestCity=i
                smallestCityCount=temp
        return smallestCity


        
        
        