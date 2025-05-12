import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort(key=lambda x:x)
        n = len(nums)
        answer=0
        previousDifference=math.inf

        for start in range(n):
            if start>0 and nums[start]==nums[start-1]: 
                continue
            
            i = start+1
            j = n-1
            while i<n and j>0 and i<j:
                newDifference =  nums[start]+nums[i]+nums[j]-target
                if abs(newDifference)<previousDifference:
                    previousDifference = abs(newDifference)
                    answer = nums[start]+nums[i]+nums[j]
                
                if newDifference>0:
                    j-=1
                elif newDifference<0:
                    i+=1
                elif newDifference==0:
                    return nums[start]+nums[i]+nums[j]
                    # i+=1
                    # while i<n and nums[i]==nums[i-1]: continue
        return answer

        