# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None: return head
        slowPointer = head
        fastPointer = head
        prev = None
        while fastPointer is not None and fastPointer.next is not None:
            prev = slowPointer
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        
        #Reverse the 2nd half
        if prev is not None: prev.next = None
        curr = slowPointer
        prev = None
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        secondLLReference = prev

        firstLLReference = head
        count=0
        while firstLLReference is not None and secondLLReference is not None:
            if count%2==0:
                backup = firstLLReference.next
                firstLLReference.next = secondLLReference
                firstLLReference = backup
            else:
                backup = secondLLReference.next
                secondLLReference.next = firstLLReference
                secondLLReference = backup
            count+=1
            
        return head

        
