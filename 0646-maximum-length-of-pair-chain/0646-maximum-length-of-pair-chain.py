class Solution:
    def findLongestChain(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:(x[1],x[0]))
        prev_start = float("-inf")
        prev_end = float("-inf")
        length = 0
        for curr_start,curr_end in intervals:
            if curr_start>prev_end:
                #we can pick this
                length+=1
                prev_end = curr_end
        return length


