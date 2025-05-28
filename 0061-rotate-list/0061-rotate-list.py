# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        pointer = head
        length = 0
        while pointer is not None: 
            pointer = pointer.next
            length+=1
        
        dummy = ListNode(0,head)
        if dummy.next is None or dummy.next.next is None: return dummy.next
        for _ in range(k%length):
            prev = dummy
            curr = dummy.next
            while curr is not None and curr.next is not None:
                nxtBackup = curr.next
                prev = curr
                curr = nxtBackup
            prev.next = None
            curr.next = dummy.next
            dummy.next = curr
            
            
        
        return dummy.next

        