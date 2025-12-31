from math import ceil
class Solution:
    def possible_to_eat_in_k(self,piles,k,h):
        time = 0
        for pile in piles:
            time+=ceil(pile/k)
        return time<=h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)+1
        ans = float("inf")
        while l<r:
            m = (l+r)//2
            if self.possible_to_eat_in_k(piles,m,h):
                ans = m
                r = m
            else:
                l = m+1
        return ans

        
