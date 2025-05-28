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

        if head is None or head.next is None: return head

        
        prev = None
        slowPointer = head
        fastPointer = head

        while fastPointer is not None and fastPointer.next is not None:
            prev = slowPointer
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        #Reverse this half
        currentNodeBackup = prev
        curr = slowPointer
        while curr is not None:
            nextBackup = curr.next
            curr.next = prev
            prev = curr
            curr = nextBackup
        currentNodeBackup.next.next = None
        currSecondHalf = prev

        currentNodeBackup.next = None

        currFirstHalf = head

        while   currFirstHalf is not None and currSecondHalf is not None:
            nextFirstHalf = currFirstHalf.next if currFirstHalf is not None else None
            nextSecondHalf = currSecondHalf.next if currSecondHalf is not None else None
            
            if currFirstHalf is not None:
                currFirstHalf.next = currSecondHalf 
            if currSecondHalf is not None:
                currSecondHalf.next = nextFirstHalf 
            if nextFirstHalf is None and nextSecondHalf is not None:
                currSecondHalf.next = nextSecondHalf

            
            currFirstHalf = nextFirstHalf
            currSecondHalf = nextSecondHalf
   

        return head




        