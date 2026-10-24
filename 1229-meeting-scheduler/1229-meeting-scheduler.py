class Solution:
    def minAvailableDuration(self, slots1: list[list[int]], slots2: list[list[int]], duration: int) -> list[int]:
        slots1.sort(key=lambda x:x[0])
        slots2.sort(key=lambda x:x[0])
        pi = 0
        pj = 0
        n = len(slots1)
        m = len(slots2)
        while pi<n and pj<m:
            
            if slots1[pi][1]<slots2[pj][0]:
                pi+=1
            elif slots2[pj][1]<slots1[pi][0]:
                pj+=1
            else:
                common_slot_start,common_slot_end = [max(slots1[pi][0],slots2[pj][0]),min(slots1[pi][1],slots2[pj][1])]
                if common_slot_end-common_slot_start>=duration:
                    return [common_slot_start,common_slot_start+duration]
                if slots1[pi][1]>slots2[pj][1]:
                    pj+=1
                else:
                    pi+=1
        return []
        

        