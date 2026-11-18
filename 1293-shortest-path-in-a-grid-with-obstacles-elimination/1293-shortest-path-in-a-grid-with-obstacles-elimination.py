class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        visited = set()
        #we define nodes to be (r,c,moves)
        m = len(grid)
        n = len(grid[0])
 
        queue = deque([(0,0,k,0)])
        while queue:
            r,c,removals_left,curr_steps = queue.popleft()
            if r==m-1 and c==n-1: return curr_steps
            visited.add((r,c,removals_left))
            #explore all neighbours of this
            for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr,nc = dr + r,dc + c
                if nr in [-1,m] or nc in [-1,n]: continue
                #two cases- obstacle there in which case we remove it, and second if obstacles is not there
                if removals_left>0 and grid[nr][nc]==1 and (nr,nc,removals_left-1) not in visited:
                    visited.add((nr,nc,removals_left-1))
                    queue.append((nr,nc,removals_left-1,curr_steps+1))
                
                if grid[nr][nc]==0 and (nr,nc,removals_left) not in visited:
                    visited.add((nr,nc,removals_left))
                    queue.append((nr,nc,removals_left,curr_steps+1))
            

        return -1