class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        #goal-> minimize the maximum value across a path leading to n-1,n-1
        #dijisktra algorithm-> oelgv
        n = len(grid)
        min_heap = [] #cost so far (= max node value),row,col
        visited = set() #r,c
        heapq.heappush(min_heap,(grid[0][0],0,0))
        while min_heap:
            curr_cost,r,c = heapq.heappop(min_heap)
            if (r,c) in visited: continue
            if r==n-1 and c==n-1: return curr_cost
            visited.add((r,c))
            for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr = dr + r
                nc = dc + c
                if nr in [-1,n] or nc in [-1,n] or (nr,nc) in visited: continue
                #new cost of this move will be the max of curr cost and this move
                new_cost = max(curr_cost,grid[nr][nc])
                heapq.heappush(min_heap,(new_cost,nr,nc))
        return -1





        