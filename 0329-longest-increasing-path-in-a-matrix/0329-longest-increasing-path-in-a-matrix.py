class Solution:
    
        


    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[-1 for _ in range(m+10)] for _ in range(n+10)]
        ans=0


        def dfs(i,j):
            if dp[i][j]!=-1: return dp[i][j]
            dirs = [(-1,0),(1,0),(0,1),(0,-1)]
            ans=-1
            for (di,dj) in dirs:
                iNew = i+di
                jNew = j+dj
                if(iNew>=0 and jNew>=0 and iNew<len(matrix) and jNew<len(matrix[0])):
                    if matrix[iNew][jNew]>matrix[i][j]:
                        ans = max(ans,1+dfs(iNew,jNew))
            if ans==-1:
                dp[i][j]=1
            else:
                dp[i][j]=ans
            return dp[i][j]


        for i in range(n):
            for j in range(m):
                if dp[i][j]==-1:
                    ans = max(ans,dfs(i,j))
        return ans
                    
        