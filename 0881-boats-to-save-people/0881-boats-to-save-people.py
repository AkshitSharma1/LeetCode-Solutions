class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        boats_required = 0
        people.sort()
        l = 0
        r = n-1
        while l<r:
            combined_weight = people[l]+people[r]
            if combined_weight<=limit:
                boats_required+=1
                l+=1
                r-=1
            else:
                boats_required+=1
                r-=1
        if l==r: boats_required+=1
        return boats_required
       

