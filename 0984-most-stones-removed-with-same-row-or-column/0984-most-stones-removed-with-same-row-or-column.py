from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        adjList = defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0]==stones[j][0] or stones[j][1]==stones[i][1]:
                    adjList[i].append(j)
                    adjList[j].append(i)
            
        
        visited = set()
        
        def dfs(index):
            if index in visited: return
            visited.add(index)
            for neighbour in adjList[index]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        stoneGroupsCount=0
        for stone in range(n):
            if stone not in visited:
                dfs(stone)
                stoneGroupsCount+=1
        
        return n-stoneGroupsCount


                
        
        