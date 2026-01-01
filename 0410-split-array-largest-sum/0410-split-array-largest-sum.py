from math import ceil
class Solution:
    def is_possible_with_maxsum_k(self,nums,mid,k):
        running_sum = 0
        splits_count = 1
        for num in nums:
            if num+running_sum<=mid:
                running_sum+=num
            else:
                splits_count+=1
                running_sum = num
                if running_sum>mid: return False
        return splits_count<=k
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = max(nums)
        r = max(nums)*(ceil(n/k)+1)

        answer = 0
        while l<r:
            mid = (l+r)//2
            if self.is_possible_with_maxsum_k(nums,mid,k):
                r = mid
                answer = mid

            else:
                l = mid+1
        return answer



        
        