# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(float("-inf"),head)
        curr = dummy
        while curr.next:
            if curr.next.val==curr.val:
                #remove the next node
                curr.next = curr.next.next
            else:
                #move curr to the next node
                curr = curr.next
        return dummy.next