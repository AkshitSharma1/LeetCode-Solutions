# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseLinkedList(self,head):
        if head.next is None: return head
        curr = head
        prev = None

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev #The new head

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        l1ReversedHead = self.reverseLinkedList(l1)
        l2ReversedHead = self.reverseLinkedList(l2)

        l1ReversedPointer = l1ReversedHead
        l2ReversedPointer = l2ReversedHead

        dummyHead = ListNode(0,None)
        pointer = dummyHead
        carry=0
        while l1ReversedPointer is not None or l2ReversedPointer is not None:
            sumOfValues= (l1ReversedPointer.val if l1ReversedPointer is not None else 0) + (l2ReversedPointer.val if l2ReversedPointer is not None else 0) + carry
            l1ReversedPointer = l1ReversedPointer.next if l1ReversedPointer is not None else None
            l2ReversedPointer = l2ReversedPointer.next if l2ReversedPointer is not None else None

            carry = sumOfValues//10
            pointer.next = ListNode(sumOfValues%10,None)
            pointer = pointer.next
        
        if carry!=0:
            pointer.next = ListNode(1,None)
            pointer = pointer.next
        
        return self.reverseLinkedList(dummyHead.next)
        
        

            

    
        