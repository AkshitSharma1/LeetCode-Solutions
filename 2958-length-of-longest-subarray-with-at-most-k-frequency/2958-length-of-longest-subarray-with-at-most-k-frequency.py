class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        n = len(nums)        
        max_length = 0
        l = 0
        for r in range(n):
            freq[nums[r]]+=1
            while freq[nums[r]]>k:
                freq[nums[l]]-=1
                l+=1
            max_length = max(max_length,r-l+1)
        return max_length