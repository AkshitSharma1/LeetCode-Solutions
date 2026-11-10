class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        flower_boom_delta =defaultdict(int)
        for flower_start,flower_end in flowers:
            flower_boom_delta[flower_start]+=1
            flower_boom_delta[flower_end+1]-=1
        
        flower_boom = {}
        running_count = 0
        for day,flower_delta in sorted(list(flower_boom_delta.items()),key=lambda x:x[0]):
            running_count += flower_delta
            flower_boom[day] = running_count
        
        flower_boom_days = sorted(flower_boom.keys())
        answer = []
        for arrival_time in people:
            index = bisect_right(flower_boom_days,arrival_time)-1
            if index==-1:
                answer.append(0)
                continue
            else:
                answer.append(flower_boom[flower_boom_days[index]])
        
        return answer
        


            