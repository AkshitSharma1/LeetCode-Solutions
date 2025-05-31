from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visitedSet = set()
        m = len(grid)
        n = len(grid[0])
        rottingTimes = [[-1]*n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if grid[r][c]==2:
                    queue.append((r,c))
                    rottingTimes[r][c]=0
                 
        
        while queue:
            currR,currC = queue.popleft()
            for dR,dC in [(-1,0),(1,0),(0,1),(0,-1)]:
                newR,newC = currR+dR,currC+dC
                if newR<0 or newC<0 or newR>=m or newC>=n: continue
                if grid[newR][newC]==1:
                    grid[newR][newC]=2
                    rottingTimes[newR][newC] = rottingTimes[currR][currC]+1
                    queue.append((newR,newC))

        answer = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1: return -1
                answer = max(answer,rottingTimes[r][c])
        return answer
        