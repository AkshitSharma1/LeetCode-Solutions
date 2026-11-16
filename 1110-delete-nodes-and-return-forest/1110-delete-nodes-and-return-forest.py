# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest = []
        def removeOnes(node):
            #removes all the ones in the subtree having root as node
            # also adds all the forests as a result of this to the array
            nonlocal forest,to_delete
            if node is None: return node
            #first call it for the childs
            node.left = removeOnes(node.left)
            node.right = removeOnes(node.right)

            if node.val not in to_delete: return node
            #if this node is to be removed
            for child in [node.left,node.right]:
                if child is None: continue
                forest.append(child)
            
            return None
        root = removeOnes(root)
        if root is not None: forest.append(root)
        return forest

