class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        best_ans = 0
        ans = 0
        for num in num_set:
            
            if num-1 in num_set:continue
            ans = 0
            while num in num_set:
                ans+=1
                num+=1
                best_ans = max(best_ans,ans)
        return best_ans