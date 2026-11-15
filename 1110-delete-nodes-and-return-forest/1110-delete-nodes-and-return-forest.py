# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        #first process each child, and then check if root is to be removed
        #in that case- number of forest = 0,1 or 2 depending upon number of child
        answer = []
        to_delete = set(to_delete)
        def removeNodes(node):
            nonlocal to_delete
            #basecase
            if node is None: return None

            node.left = removeNodes(node.left)
            node.right = removeNodes(node.right)

            #now check if node.val==to delete or not
            # if it is-we will get either 0,1 or 2 forests
            if node.val in to_delete:
                for child in [node.left,node.right]:
                    if child is None: continue
                    answer.append(child)
                return None
            return node
        
        root = removeNodes(root)
        if root is not None:
            answer.append(root)
        
        return answer