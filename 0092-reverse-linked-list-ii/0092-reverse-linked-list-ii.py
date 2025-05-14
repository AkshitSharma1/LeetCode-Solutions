# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummyHead = ListNode(0,head)
        prev = dummyHead
        curr = head
        nxt = curr.next

        position=1

        while position<left:
            prev = curr
            curr = curr.next
            nxt = curr.next
            position+=1
        

        beforeReversalNode = prev
        #Now we reverse this, upto length k iteratively
        while position<=right:
            nextToNext = nxt.next if nxt is not None else None
            
            
            curr.next = prev
            
            prev = curr
            curr = nxt
            nxt = nextToNext
            position+=1
        
        if beforeReversalNode is not None and beforeReversalNode.next is not None:
            beforeReversalNode.next.next = curr
        if beforeReversalNode.next is not None:
            beforeReversalNode.next = prev

        return dummyHead.next






            
        
        
        return head

        