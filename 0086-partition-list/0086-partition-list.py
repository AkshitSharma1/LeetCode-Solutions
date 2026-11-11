# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        less_head = ListNode(-1,None)
        less_pointer = less_head
        big_head = ListNode(-1,None)
        big_pointer = big_head

        curr = head
        while curr:
            if curr.val<x:

                less_pointer.next = curr
                less_pointer = curr
            else:
                big_pointer.next = curr
                big_pointer = curr
            
            curr = curr.next
        
        less_pointer.next = big_head.next
        big_pointer.next = None
        return less_head.next