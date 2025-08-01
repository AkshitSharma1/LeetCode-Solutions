class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monotonicQueue = deque()
        ans = []
        for r,num in enumerate(nums):
            while monotonicQueue and nums[monotonicQueue[-1]]<num:
                monotonicQueue.pop()
            monotonicQueue.append(r)
            while monotonicQueue and monotonicQueue[0]<r-k+1:
                monotonicQueue.popleft()
            if r-k+1>=0:
                ans.append(nums[monotonicQueue[0]])
        return ans
        