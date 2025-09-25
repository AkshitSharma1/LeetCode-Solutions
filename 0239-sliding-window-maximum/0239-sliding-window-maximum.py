class Solution:


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        slidingWindow = deque()
        answer = []
        for r,num in enumerate(nums):
            while slidingWindow and nums[slidingWindow[-1]]<=num:
                slidingWindow.pop()
            slidingWindow.append(r)
            if r>=k-1:
                while slidingWindow and slidingWindow[0]<r-k+1:
                    slidingWindow.popleft()
                answer.append(nums[slidingWindow[0]])
        return answer
            
                
        
        