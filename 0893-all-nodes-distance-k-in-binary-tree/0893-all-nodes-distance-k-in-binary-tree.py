# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List

class Solution:
    def distanceK(self, root: 'TreeNode', target: 'TreeNode', k: int) -> List[int]:
        result = []

        def collectDown(node: 'TreeNode', dist: int) -> None:
            if not node:
                return
            if dist == k:
                result.append(node.val)
                return
            collectDown(node.left, dist + 1)
            collectDown(node.right, dist + 1)

        def dfs(node: 'TreeNode') -> int:
            """
            Returns distance from 'node' to 'target', or -1 if target not in this subtree.
            While unwinding, collect nodes on the opposite subtree at the needed remaining distance.
            """
            if not node:
                return -1
            if node is target:
                collectDown(node, 0)  # include all nodes k below target (handles k==0 too)
                return 1

            leftDistance = dfs(node.left)
            if leftDistance != -1:
                # target is in left subtree; current node is at leftDistance+1 from target
                if leftDistance == k:
                    result.append(node.val)
                elif leftDistance<k:
                    # need to go into right subtree to collect nodes at (k - (leftDistance+2)) below right
                    collectDown(node.right, leftDistance + 1)
                return leftDistance + 1

            rightDistance = dfs(node.right)
            if rightDistance != -1:
                if rightDistance + 0 == k:
                    result.append(node.val)
                elif rightDistance<k:
                    collectDown(node.left, rightDistance + 1)
                return rightDistance +1

            return -1

        dfs(root)
        return result
