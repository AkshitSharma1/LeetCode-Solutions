class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        candidates = [x for x in range(1,10)]
        answer = []
        curr_answer = []
        candidates.sort()
        def solution(index,new_target,curr_answer,k_left):
            if new_target<0 or k_left<0: return
            if new_target==0 and k_left==0:
                answer.append(curr_answer.copy())
                return
            #pick or no pick
            for i,num in enumerate(candidates[index:]):
                #pick
                if i>0 and candidates[i+index]==candidates[i-1+index]: continue
                curr_answer.append(num)
                solution(index+i+1,new_target-num,curr_answer,k_left-1)
                curr_answer.pop()
        solution(0,target,curr_answer,k)
        return answer

    