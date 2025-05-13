# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Find length of both linkedList
        l1Pointer = l1
        l2Pointer = l2
        l2Length = 0
        l1Length = 0
        while l1Pointer is not None:
            l1Length+=1
            l1Pointer = l1Pointer.next
        
        while l2Pointer is not None:
            l2Length+=1
            l2Pointer = l2Pointer.next
        base = l1
        if l1Length>=l2Length:
            p1, p2 = l1,l2
            base = l1
        else:
            p1,p2 = l2,l1
            base = l2
        

        carry = 0
        while p1 is not None:
            sumOfValues = (p1.val + (p2.val if p2 is not None else 0) + carry)
            p1.val = sumOfValues % 10
            carry = sumOfValues // 10

            print(carry)

            if p1.next is None and carry!=0:
                p1.next =  ListNode(val=0,next=None)
                
            p1 = p1.next
            if p2 is not None:
                p2 = p2.next
        
        
        return base
        