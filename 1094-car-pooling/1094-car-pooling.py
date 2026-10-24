class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        transitions = [] #(time,#passenger) array ,
        for num_passenger,fro,destination in trips:
            transitions.append((fro,+num_passenger))
            transitions.append((destination,-num_passenger))
        transitions.sort(key=lambda x:(x[0],x[1]))
        running_passenger_count = 0
        for time,new_passenger_count in transitions:
            running_passenger_count+=new_passenger_count
            if running_passenger_count>capacity:
                return False
        
        return True