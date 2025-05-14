# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Check number of nodes beyond head - if less than k nodes, just return  
        pointer = head
        length = 0
        while pointer is not None and length<k:
            pointer = pointer.next
            length +=1
        if length<k: return head

        dummyHead = ListNode(0,head)
        prev = dummyHead
        curr = head
        nxt = curr.next
        previousNodeBackup = prev
        for _ in range(k):
            nextNodeBackup = nxt
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt
        
        previousNodeBackup.next.next = self.reverseKGroup(curr,k)
        previousNodeBackup.next = prev
        return dummyHead.next
        


