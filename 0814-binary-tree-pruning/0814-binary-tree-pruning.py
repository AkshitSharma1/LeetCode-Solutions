# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode | None) -> TreeNode | None:
        def containsOne(node):
            #basecase
            if node is None:
                return False,None

            #returns true or false accordingly along witht the new root node (which is the child for the parent node)
            left_child_contains_one, left_child = containsOne(node.left)
            right_child_contains_one, right_child = containsOne(node.right)

            if  left_child_contains_one==False:
                node.left = None
            else:
                node.left = left_child

            
            if right_child_contains_one==False:
                node.right = None
            else:
                node.right = right_child

            
            #post removal- both the childs are none now
            if node.val!=1 and node.left is None and node.right is None:
                return False,None
            
            return True,node
        _,root =  containsOne(root)
        return root

            
            
        