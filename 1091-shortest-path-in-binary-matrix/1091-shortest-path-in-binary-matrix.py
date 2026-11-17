class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        queue = deque([(1,0,0)]) #dist,row,col
        visited = set()
        n = len(grid)
        visited.add((0,0))
        if grid[0][0]==1: return -1
        while queue:
            dist,row,col = queue.popleft()
            visited.add((row,col))
            if row==n-1 and col==n-1: return dist
            for dr,dc in [(-1,-1),(-1,1),(-1,0),(0,1),(0,-1),(1,0),(1,1),(1,-1)]:
                new_r = row + dr
                new_c = col + dc
                if new_r<0 or new_r>=n or new_c<0 or new_c>=n: continue
                if (new_r,new_c) in visited or grid[new_r][new_c]!=0: continue
                queue.append((dist+1,new_r,new_c))
                visited.add((new_r,new_c))
        return -1
