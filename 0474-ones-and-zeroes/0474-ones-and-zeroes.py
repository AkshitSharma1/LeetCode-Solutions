class Solution:
    
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def getZeroCount(string):
            return string.count("0")
        def getOneCount(string):
            return string.count("1")
        zeroCount = defaultdict(int)
        oneCount = defaultdict(int)
        for string in strs:
            zeroCount[string] = getZeroCount(string)
            oneCount[string] = getOneCount(string)
        
        dp = [[[-1]*(n+1) for _ in range(m+1)] for _ in range(len(strs))]
        def f(index,mLeft,nLeft):
            if mLeft<0 or nLeft<0: return -1e7
            if index>=len(strs): return 0
            if dp[index][mLeft][nLeft] !=-1: return dp[index][mLeft][nLeft]

            dp[index][mLeft][nLeft] = max(f(index+1,mLeft,nLeft),1+f(index+1,mLeft-zeroCount[strs[index]],nLeft-oneCount[strs[index]]))
            return dp[index][mLeft][nLeft]
        
        return f(0,m,n)
        