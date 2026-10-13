class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        running_sum = 0
        ans = 0
        prefix_sum_count[0] = 1
        for num in nums:
            running_sum += num
            difference = running_sum-k
            if difference==0:
                ans += (prefix_sum_count[0])
            else:
                ans += (prefix_sum_count[difference])

            prefix_sum_count[running_sum] +=1
        return ans



        