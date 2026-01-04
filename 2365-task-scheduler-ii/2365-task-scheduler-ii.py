class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_performed = defaultdict(lambda:-1)
        day = 1
        for task in tasks: #5,8,8,5
            if last_performed[task]==-1 or last_performed[task]+space+1<day:
                last_performed[task] = day
            else:
                day = last_performed[task] + space + 1
                last_performed[task]= day
            day+=1
        
        return day -1