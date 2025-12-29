class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monotonic_queue = deque()
        answer = []
        
        for r,num in enumerate(nums):
            while monotonic_queue and nums[monotonic_queue[-1]]<num:
                monotonic_queue.pop()
            monotonic_queue.append(r)

            while monotonic_queue and monotonic_queue[0]<r+1-k:
                monotonic_queue.popleft()
            if r+1-k>=0: answer.append(nums[monotonic_queue[0]])
        return answer




