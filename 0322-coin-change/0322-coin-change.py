class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        @cache
        def dp(amount_left,index):
            #minimum number of coins from 0 to index inclusive indexes which we can use to reduce amount_left to 0
            #two cases-> take the coin, do not take the coin
            # we want dp(amount,len(coins)-1)
            if amount_left<0 or index<0: return float("inf")

            if amount_left==0: 
                return 0


            answer = min(
                dp(amount_left,index-1), 1 + dp(amount_left-coins[index],index)
            )
            return answer
        answer = dp(amount,len(coins)-1)
        return answer if answer<float("inf") else -1