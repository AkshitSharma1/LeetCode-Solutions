class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def countPairs(currentString,unbalanceCount):
            if len(currentString)==2*n:
                if unbalanceCount==0: ans.append(currentString)
                return
            
            countPairs(currentString+"(",unbalanceCount+1)
            if unbalanceCount>0:
                countPairs(currentString+")",unbalanceCount-1)
        countPairs("",0)
        return ans
        