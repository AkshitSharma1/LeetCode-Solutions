# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: TreeNode | None, startValue: int, destValue: int) -> str:
        def findPath(node,value,path):
            #given node,value,path- recursively find the path to the node having val as value and store its path
            if node is None: return None
            if node.val==value:
                #this is the ans, append it to path and return the node
                return True
            #try moving left
            path.append("L")
            left_subtree = findPath(node.left,value,path)
            if left_subtree:
                return True
            #left moving failed, so we move to the right
            path.pop()
            path.append("R")
            right_subtree = findPath(node.right,value,path)
            if right_subtree:
                return True
            #none works- this node doesnt contain answer in its childs
            path.pop()
            return False

        root_to_start = []
        root_to_target = []
        findPath(root,startValue,root_to_start)
        findPath(root,destValue,root_to_target)
        #now remove common prefix
        i = 0
        n = len(root_to_start)
        m = len(root_to_target)
        while i<min(len(root_to_start),len(root_to_target)) and root_to_start[i]==root_to_target[i]:
            i+=1
        #i now points to the index which is not common (assuming paths do not overlap)
        #2 edge cases-> i = path length
        answer = []
        if i<n and i<m:
            #we go up n-i times
            for _ in range(n-i): answer.append("U")
            answer.extend(root_to_target[i:])
            return "".join(answer)
        elif i==n:
            #start node lies on path of destination
            return "".join(root_to_target[i:])
        
        elif i==m:
            #destination lies on path from start upwards
            for _ in range(n-i): answer.append("U")
        return "".join(answer)
