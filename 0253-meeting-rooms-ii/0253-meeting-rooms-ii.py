class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        concurrentMeetCount = defaultdict(int)
        for interval in intervals:
            concurrentMeetCount[interval[0]]+=1
            concurrentMeetCount[interval[1]]-=1
        
        #Now sort this
        maxConcurrentMeet = 0
        answer = 0
        for time in sorted(concurrentMeetCount.keys()):
            maxConcurrentMeet+=concurrentMeetCount[time]
            answer = max(answer,maxConcurrentMeet)
        return answer
