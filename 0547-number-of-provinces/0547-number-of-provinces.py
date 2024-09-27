class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #Adjacency matrix
        visited = set()
        n = len(isConnected)


        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for neighbour in range(n):
                if neighbour not in visited and isConnected[i][neighbour]==1:
                    dfs(neighbour)
            



        count=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        return count
        