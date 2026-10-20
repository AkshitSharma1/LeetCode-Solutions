class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],x[1]))
        ans = [intervals[0]]
        for interval in intervals[1:]:
            #c1- this covers the earlier interval
            if ans[-1][0]>=interval[0] and ans[-1][1]<=interval[1]:
                ans.pop()
                ans.append(interval)
                continue
            #c2 this is covered by earlier interval
            if ans[-1][0]<=interval[0] and ans[-1][1]>=interval[1]:
                continue
            
            ans.append(interval)
        return len(ans)


        