class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        task_names = set(tasks)
        last_performed = {task_name:-1 for task_name in task_names}
        curr_day = 0
        i = 0
        while i<len(tasks):
            task = tasks[i]
            if last_performed[task]==-1:
                #perform the task
                last_performed[task] = curr_day
                curr_day+=1
                i+=1
            else:
                if (curr_day-last_performed[task]-1>=space):
                    last_performed[task] = curr_day
                    curr_day +=1
                    i+=1
                else:
                    curr_day += (last_performed[task]+space+1)-curr_day
        return curr_day
