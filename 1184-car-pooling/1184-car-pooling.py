class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips,key=lambda x:(x[1],x[2]))
        
        partialSum = [0]*1001
        for trip in trips:
            partialSum[trip[1]]+=trip[0]
            partialSum[trip[2]]-=trip[0]
        prefixSum=[0]*1001
        for i in range(1001):
            if i>0: prefixSum[i]=prefixSum[i-1]
            prefixSum[i] += partialSum[i]
            if prefixSum[i]>capacity: return False
        return True

