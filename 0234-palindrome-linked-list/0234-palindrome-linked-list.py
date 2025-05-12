# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Aliter: O(N) time complexity + O(1) space complexity
        '''
        Find middle of Linkedlist using slow and fast pointer
        Reverse 2nd half of linkedlist and compare head 2nd half head
        '''

        slowPointer = head
        fastPointer = head
        while  fastPointer is not None and fastPointer.next is not None:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        
        current,previous = slowPointer,None
        while current is not None:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        
        secondHalfHead = previous
        firstHalfHead = head
        while firstHalfHead is not None and secondHalfHead is not None:
            if firstHalfHead.val != secondHalfHead.val: return False
            firstHalfHead = firstHalfHead.next
            secondHalfHead = secondHalfHead.next
        return True
            
        