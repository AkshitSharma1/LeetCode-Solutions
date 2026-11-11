# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(-1,list1)
        prev = dummy
        curr = list1
        for _ in range(a):
            prev = curr
            curr = curr.next
        
        #remove this node, while retaining its next pointer
        nxt = curr.next
        prev.next = list2
        prev = curr
        curr = curr.next
        #find the node just after bth node

        for _ in range(b-a): curr = curr.next

        #find list2 end
        list2_end = list2
        while list2_end.next: list2_end = list2_end.next
        list2_end.next = curr
        return dummy.next
