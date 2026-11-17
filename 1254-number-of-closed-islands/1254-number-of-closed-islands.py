class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        #n*m grid


        def labelNodes(i,j):
            nonlocal grid,m,n
            #will label all nodes connected to (i,j) with -1
            if grid[i][j]!=0: return
            grid[i][j]=-1

            for di,dj in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_i = di + i
                new_j = dj + j
                if new_i<0 or new_i>=n or new_j<0 or new_j>=m: continue
                if grid[new_i][new_j]==0:
                    labelNodes(new_i,new_j)
            
            return
        def dfs(i,j):
            nonlocal visited
            if (i,j) in visited: return
            visited.add((i,j))
            for di,dj in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_i = di + i
                new_j = dj + j
                if new_i<0 or new_i>=n or new_j<0 or new_j>=m: continue
                if grid[new_i][new_j]==0:
                    dfs(new_i,new_j)


        

        for i in range(n):
            for j in range(m):
                if (i in [0,n-1] or j in [0,m-1]) and grid[i][j]==0:
                    labelNodes(i,j)
        
        #now count number of connected components of 0s
        closed_island_count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0 and (i,j) not in visited:
                    dfs(i,j)
                    closed_island_count+=1


        return closed_island_count
                    