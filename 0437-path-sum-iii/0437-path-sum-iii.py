# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefix_sum_freq = defaultdict(int)
        prefix_sum_freq[0] = 1
        answer = 0

        def dfs(node,curr_sum):
            if node is None:
                return

            nonlocal answer
            curr_sum+=node.val
            difference = curr_sum-targetSum
            #now we check freq of occurence of difference 
            answer += prefix_sum_freq[difference]
            prefix_sum_freq[curr_sum]+=1

            dfs(node.left,curr_sum)
            dfs(node.right,curr_sum)
            prefix_sum_freq[curr_sum]-=1
            return
        dfs(root,0)
        return answer




        
    
