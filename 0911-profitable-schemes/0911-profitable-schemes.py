class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        #index,groupmembers,profit
        MOD = 1e9+7
        maxProfitPossible = sum(profit)
        dp = [[[-1]*(minProfit+1) for _ in range(n+1)] for _ in range(len(profit))]
        def f(index,groupMembersLeft,profitMadeSoFar):
            if groupMembersLeft<0: return 0
            if profitMadeSoFar>=minProfit: profitMadeSoFar = minProfit
            if index==len(group):
                if profitMadeSoFar>=minProfit: return 1
                return 0
            if dp[index][groupMembersLeft][profitMadeSoFar]!=-1: return dp[index][groupMembersLeft][profitMadeSoFar]
            dp[index][groupMembersLeft][profitMadeSoFar] =   int((f(index+1,groupMembersLeft-group[index],profitMadeSoFar+profit[index])%MOD + f(index+1,groupMembersLeft,profitMadeSoFar)%MOD)%MOD)
            
            return dp[index][groupMembersLeft][profitMadeSoFar]
        
        return f(0,n,0)

            
            