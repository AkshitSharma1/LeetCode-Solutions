class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        people_at_time = defaultdict(int)
        for num_passengers,fro,to in trips:
            people_at_time[fro]+=num_passengers
            people_at_time[to]-=num_passengers
        
        sorted_time = sorted(people_at_time.keys())
        people_inside = 0
        for time in sorted_time:
            people_inside +=people_at_time[time]
            if people_inside>capacity:
                return False
        return True

