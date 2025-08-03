class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        freeTimes = []
        freeTimes.append(startTime[0]-0)
        for i in range(1,len(startTime)):
            freeTimes.append(startTime[i]-endTime[i-1])
        
        freeTimes.append(eventTime-endTime[len(endTime)-1])

        maxSum = 0
        answer = 0
        l=0
        for r in range(len(freeTimes)):
            maxSum +=freeTimes[r]
            while r-l+1>k+1:
                maxSum-=freeTimes[l]
                l+=1
            
            answer = max(answer,maxSum)
        return answer

        