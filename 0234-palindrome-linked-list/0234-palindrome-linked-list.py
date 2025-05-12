# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        pointer = head
        while pointer is not None:
            stack.append(pointer.val)
            pointer = pointer.next
        
        while len(stack)>0:
            if stack.pop()!=head.val: return False
            head = head.next
        return True

        