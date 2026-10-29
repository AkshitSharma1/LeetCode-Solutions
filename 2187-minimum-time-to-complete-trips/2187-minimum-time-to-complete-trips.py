class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        def countTripsInTime(given_time):
            num_trips = 0
            for curr_bus_time in time: num_trips+=given_time//curr_bus_time
            return num_trips
        

        l = 0
        r = max(time)*totalTrips #max time possible
        #we will apply binar serch over time
        ans = float("inf")
        while l<=r:
            m = (l+r)//2
            if countTripsInTime(m)>=totalTrips:
                ans = min(ans,m)
                #now search for smaller time
                r = m-1
            else:
                #not possible, so try a bigger time
                l = m+1
        return ans
