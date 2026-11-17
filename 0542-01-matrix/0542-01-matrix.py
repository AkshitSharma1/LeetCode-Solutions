class Solution:
    def updateMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        queue = deque()
        visited = set()
        m = len(grid)
        n = len(grid[0])
        dist = [[float("inf")]*n for _ in range(m)]
        #m*n matrix

        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    queue.append((0,r,c))
                    visited.add((r,c))
                    dist[r][c] = 0
        
        while queue:
            curr_dist,r,c = queue.popleft()
            #explore neighbours
            for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr = r +dr
                nc = c + dc
                if nr in [-1,m] or nc in [-1,n] or (nr,nc) in visited or grid[nr][nc]==0: continue
                dist[nr][nc] = curr_dist+1
                queue.append((curr_dist+1,nr,nc))
                visited.add((nr,nc))
        return dist

