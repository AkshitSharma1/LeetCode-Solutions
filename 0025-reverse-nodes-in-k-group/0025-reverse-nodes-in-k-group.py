# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lengthPointer = head
        count = 0
        while lengthPointer is not None and count<k:
            lengthPointer = lengthPointer.next
            count+=1
        if count<k:
            return head
        

        #Reverse the first k nodes
        prev = None
        curr = head
        nxt = curr.next
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        

        #Link it to next node
        head.next = self.reverseKGroup(curr,k)
        return prev
        