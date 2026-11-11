# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1,head)
        prev = dummy
        curr = head
        while curr:
            duplicate_count = 0
            while curr and curr.next and curr.next.val==curr.val:
                #duplicates, keep on skipping this
                curr = curr.next
                duplicate_count+=1
            
            if duplicate_count==0:
                #no duplicates , can safely increment both prev and curr
                prev = curr
                curr = curr.next
            else:
                #we had duplicates, curr.next will resemble first non-duplicate element
                prev.next = curr.next
                curr = curr.next
                #its possible that this new number might also have duplicates, so we dont increase prev
        return dummy.next
