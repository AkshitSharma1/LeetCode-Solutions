class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        
        nums.sort()
        #now more index ifference means farther number
        l = 0
        n = len(nums)
        r = 10**6+1
        def countPairsLessEqual(dist):
            lp = 0
            ans = 0
            for rp in range(n):
                #shrink the window is distance is more than dist
                while nums[rp]-nums[lp]>dist:
                    lp+=1
                if lp>rp: continue
                ans += rp-lp
            return ans
        



        #bs
        while l<r:
            m = (l+r)//2
            pairs_less_equal_m = countPairsLessEqual(m)

            #function to find number of pairs having dist <=m
            if pairs_less_equal_m>=k:
                #look at left
                r = m 
            else:
                l  = m+1
        return l

