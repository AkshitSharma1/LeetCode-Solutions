class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        dp = [[-1 for _ in range(len(s2)+3)] for _ in range(len(s1)+3)]
        def helperFunction(i,j,k):
            if dp[i][j]!=-1: return dp[i][j]
     
            if k==len(s3): 
                dp[i][j] =  True
                return dp[i][j]
          
            iMatchWithK = False
            if i<len(s1) and s1[i]==s3[k]:
                iMatchWithK = True and helperFunction(i+1,j,k+1)
            
            jMatchWithK = False
            if j<len(s2) and s2[j]==s3[k]: 
                jMatchWithK = True and helperFunction(i,j+1,k+1)
            dp[i][j] = iMatchWithK or jMatchWithK

            return dp[i][j]
        
        if len(s3)!=len(s1)+len(s2): return False
        helperFunction(0,0,0)
        return dp[0][0]
        

        
                





        