# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node
        curr = node.next
        second_prev = node
        while curr:
            prev.val = curr.val
            second_prev = prev
            prev = curr
            curr = curr.next
        second_prev.next = None

        