class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        ans = 0
        n = len(grid) #number of rows
        m = len(grid[0])

        #staircase method for counting
        # we start at bottom-left and go up or right to keep on counting (top right cordinates will be 0,m-1)
        r = n-1
        c = 0
        while c<m and r>=0:
            if grid[r][c]<0:
                #all the col to the right must also be negative
                ans += (m-c)
                r-=1 #go up
            else:
                #Grid[r][c]>=0
                #all above rows must be bigger than 0 too
                #so search on right
                c+=1
        return ans

