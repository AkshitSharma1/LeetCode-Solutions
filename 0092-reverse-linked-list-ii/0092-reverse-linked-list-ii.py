# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        #get to the required position first
        dummy = ListNode(-1,head)
        curr = dummy
        for _ in range(left-1):
            curr = curr.next
        
        prev = curr
        curr = curr.next
        #curr is the firstmost node which we reverse
        prev_backup = prev
        for _ in range(right-left+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        #curr will node point to the node just after right
        #prev points to the rght node
        prev_backup.next.next = curr
        prev_backup.next = prev
    
        return dummy.next
