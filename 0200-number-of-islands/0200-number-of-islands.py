class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        m = len(grid)
        n = len(grid[0])
        queue = deque()

        for r in range(m):
            for c in range(n):
                if  grid[r][c]=='1':
                    #Perform BFS
                    queue.append((r,c))
                    grid[r][c]='0'
                    islandCount+=1
                    while queue:
                        currR,currC = queue.popleft()

                        for dR,dC in [(-1,0),(1,0),(0,1),(0,-1)]:
                            newR,newC = currR+dR,currC+dC
                            if newR>=0 and newR<=m-1 and newC>=0 and newC<=n-1 and grid[newR][newC]=='1':
                                grid[newR][newC]='0'

                                queue.append((newR,newC))
                    
        return islandCount
                            
                
        
                
        