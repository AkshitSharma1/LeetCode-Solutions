class Solution:
    def permute(self, n: int) -> List[List[int]]:
        candidates = [i for i in range(1,n+1)]
        curr_answer = [i for i in range(1,n+1)]
        final_answer = []
        def solution(curr_index,curr_answer,last_value):
            if curr_index==n: 
                final_answer.append(curr_answer.copy())
                return
            for i,num in enumerate(candidates):
                if last_value!=-1 and (num==-1 or (last_value%2==num%2)): continue
                curr_answer[curr_index] = num
                temp = num
                candidates[i]=-1
                solution(curr_index+1,curr_answer,temp)
                candidates[i] = num
        solution(0,curr_answer,-1)
        return final_answer

