class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_value = []
        queue = deque()
        l = 0
        n = len(nums)
        for r in range(n):
            while queue and queue[-1]<nums[r]:
                 queue.pop()
                 
            queue.append(nums[r])
            while r-l+1>k:
                if nums[l]==queue[0]: queue.popleft()
                l+=1
            if r-l+1==k:  max_value.append(queue[0])
        return max_value