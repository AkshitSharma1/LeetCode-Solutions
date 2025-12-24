# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = [root]
        if root is None: return []
        ans = []
        while st:
            curr = st.pop()
            ans.append(curr.val)
            if curr.right: st.append(curr.right)
            if curr.left: st.append(curr.left)
        return ans

        