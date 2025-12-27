class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = defaultdict(lambda:0)
        nums.insert(0,1)
        nums.append(1)
        n = len(nums) -1
        #we loop from 1 to n inclusive
        for length in range(1,n+1):
            for i in range(1,n+1):
                j =i+length-1
                if j>=n: break
                for k in range(i,j+1):
                    dp[(i,j)] = max(dp[(i,j)],nums[k]*nums[i-1]*nums[j+1]+dp[(i,k-1)]+dp[(k+1,j)])
        return dp[(1,n-1)]
        

        
