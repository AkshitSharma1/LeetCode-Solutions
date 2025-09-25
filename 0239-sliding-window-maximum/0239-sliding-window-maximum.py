class Solution:


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        slidingWindow = deque()
        n = len(nums)
        l = 0
        answer = []
        for r in range(n):
            while slidingWindow and nums[slidingWindow[-1]]<nums[r]:
                slidingWindow.pop()
            slidingWindow.append(r)

            if r>=k-1:
                while slidingWindow and slidingWindow[0]<r-k+1:
                    slidingWindow.popleft()

                if slidingWindow: 
                    answer.append(nums[slidingWindow[0]])
            
        return answer



        