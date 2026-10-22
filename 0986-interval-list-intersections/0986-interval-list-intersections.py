class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        pi = 0
        pj = 0
        ans = []
    
        n = len(firstList)
        m = len(secondList)
        while pi<n and pj<m:
            #c1- pi interval is before pj interval (no overlap)
            if firstList[pi][1]<secondList[pj][0]:
                #no intersection, we move p1 ahead
                pi+=1
            #c2- pi interval is after pj interval (no overlap)
            elif firstList[pi][0]>secondList[pj][1]:
                pj+=1
            else:
                #There is overlap
                ans.append([max(firstList[pi][0],secondList[pj][0]),min(firstList[pi][1],secondList[pj][1])])
                if firstList[pi][1]<secondList[pj][1]:
                    pi+=1
                else:
                    pj+=1
        return ans
        