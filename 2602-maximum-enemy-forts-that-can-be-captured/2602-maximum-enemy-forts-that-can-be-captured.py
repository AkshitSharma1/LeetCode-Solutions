class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        moveFromLeft = [-1]*n
        moveFromRight = [-1]*n
        
        for i in range(n):
            if forts[i]==1:
                moveFromLeft[i]=0
            if forts[i]==0:
                if i>0:
                    if moveFromLeft[i-1]!=-1:
                        moveFromLeft[i]=moveFromLeft[i-1]+1
                    else:
                        moveFromLeft[i] = -1
                else: moveFromLeft[i]=-1
        for i in range(n-1,-1,-1):
            if forts[i]==1:
                moveFromRight[i]=0
            if forts[i]==0:
                if i<n-1:
                    if moveFromRight[i+1]!=-1:
                        moveFromRight[i] = moveFromRight[i+1]+1
                    else:
                        moveFromRight[i] = -1
                else:
                    moveFromRight[i] = -1
        
        ans=0

        print(moveFromRight)
        print(moveFromLeft)
        for i in range(n):
            if forts[i]==-1:
                if i>0:
                    ans = max(ans,moveFromLeft[i-1])
                if i<n-1:
                    ans = max(ans,moveFromRight[i+1])
        return ans