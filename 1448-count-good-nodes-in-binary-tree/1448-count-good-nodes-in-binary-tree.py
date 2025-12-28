# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer=0
        def recurse(root,max_val=-float("inf")):
            nonlocal answer
            if root is None: return
            if root.val>=max_val:
                max_val = root.val
                answer+=1
            recurse(root.left,max_val)
            recurse(root.right,max_val)
        recurse(root)
        return answer


        