class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        displacement = ((-1,0),(1,0),(0,1),((0,-1)))
        m = len(grid)
        n = len(grid[0])
        def bfs(r,c):
            queue.append((r,c))
            visited.add((r,c))
            numberOfNodesVisited=0
            while queue:
                currR,currC = queue.popleft()
                numberOfNodesVisited+=1

                for dR,dC in displacement:
                    newR,newC = currR+dR,currC+dC
                    if newR<0 or newC<0 or newR>=m or newC>=n: continue
                    if grid[newR][newC]==1 and (newR,newC) not in visited:
                        visited.add((newR,newC))
                        queue.append((newR,newC))
            return numberOfNodesVisited
        
        answer = 0
        for r in range(m):
            for c in range(n):
                if (r,c) not in visited and grid[r][c]==1:
                    answer = max(bfs(r,c),answer)
        return answer
        
                    
                        


                
            

        