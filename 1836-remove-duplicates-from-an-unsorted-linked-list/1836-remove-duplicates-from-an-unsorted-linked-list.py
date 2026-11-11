# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        value_count = defaultdict(int)
        counter = head
        while counter: 
            value_count[counter.val]+=1
            counter= counter.next

        dummy = ListNode(-1,head)
        prev = dummy
        curr = head
        while prev:
            while curr and value_count[curr.val]>1:
                curr = curr.next
            prev.next = curr
        
            prev = curr
            curr = curr.next if curr else None
        return dummy.next