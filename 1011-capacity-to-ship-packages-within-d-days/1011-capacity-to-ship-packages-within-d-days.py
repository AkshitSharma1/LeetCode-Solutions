from math import ceil
class Solution:
    def possible_to_ship_in_k(self,weights,k,h):
        time = 1
        curr_weight = 0
        for i in range(len(weights)):
            if curr_weight+weights[i]>k:
                time+=1
                curr_weight = weights[i]
            else:
                curr_weight+=weights[i]
        return time<=h

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)+1
        ans = float("inf")
        while l<r:
            m = (l+r)//2
            if self.possible_to_ship_in_k(weights,m,days):
                ans = m
                r = m
            else:
                l = m+1
        return ans

        
