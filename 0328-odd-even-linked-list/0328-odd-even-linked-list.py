# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        odd_head = ListNode(-1,None)
        odd_pointer = odd_head
        even_head = ListNode(-1,None)
        even_pointer = even_head
        curr = head
        i = 1
        while curr:
            if i%2==1:
                # odd node
                odd_pointer.next = curr
                odd_pointer = curr
            else:
                even_pointer.next = curr
                even_pointer = curr
            
            curr = curr.next
            i+=1
        odd_pointer.next = even_head.next
        even_pointer.next = None
        return odd_head.next
                