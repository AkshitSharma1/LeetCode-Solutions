# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(-1,head)
        curr = dummy

        while curr and curr.next:
            if curr.next.val==val:
                #remove the node
                curr.next = curr.next.next
            else:
                curr= curr.next
        return dummy.next
            
