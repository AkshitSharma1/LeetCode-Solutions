class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        answer = []
        curr_answer = []
        candidates.sort()
        def solution(index,new_target,curr_answer):
            if new_target<0: return
            if new_target==0:
                answer.append(curr_answer.copy())
                return
            #pick or no pick
            for i,num in enumerate(candidates[index:]):
                #pick
                if i>0 and candidates[i+index]==candidates[i-1+index]: continue
                curr_answer.append(num)
                solution(index+i+1,new_target-num,curr_answer)
                curr_answer.pop()
        solution(0,target,curr_answer)
        return answer


            