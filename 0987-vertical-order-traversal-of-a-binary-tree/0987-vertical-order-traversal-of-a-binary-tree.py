# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        answer = []
        def dfs(node,row,col):
            answer.append((row,col,node.val))
            if node.left:
                dfs(node.left,row+1,col-1)
            if node.right:
                dfs(node.right,row+1,col+1)
        dfs(root,0,0)
        answer.sort(key=lambda x:(x[1],x[0],x[2]))
        
        final_ans = []
        prev_col = None

        for _, col, val in answer:
            if col != prev_col:
                final_ans.append([])
                prev_col = col

            final_ans[-1].append(val)

        return final_ans
        