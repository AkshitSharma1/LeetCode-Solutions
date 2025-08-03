class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = []
        n = len(nums)
        minDifference = float("inf")
        nums.sort()
        for start in range(n):
            if start>0 and nums[start]==nums[start-1]: continue
            l,r = start+1,n-1
            while l<r:
                currentSum = nums[l]+nums[r]+nums[start]
                difference = target-currentSum
                if abs(difference)<abs(minDifference):
                    answer = [nums[start],nums[l],nums[r]]
                    minDifference = difference
                if difference>0:
                    l+=1
                elif difference<0:
                    r-=1
                else:
                    return sum(answer)
        return sum(answer)


        