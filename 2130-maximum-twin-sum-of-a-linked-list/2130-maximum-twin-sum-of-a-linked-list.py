# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        #find middle, split in two halfs
        dummy = ListNode(-1,head)
        slow = dummy
        fast = dummy
        while fast and fast.next and fast.next.next:
            fast = fast.next.next if fast.next else None
            slow = slow.next
        list2 = slow.next
        slow.next = None
        list1 = head

        #reverse list2
        dummy = ListNode(-1,list2)
        prev = dummy
        curr = list2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        dummy.next.next = None
        dummy.next = prev

        p1 = list1 #list1 pointer
        p2 = dummy.next #list2 pointer
        max_sum = 0
        while p1 is not None and p2 is not None:
            max_sum = max(max_sum,p1.val+p2.val)
            p1 = p1.next
            p2 = p2.next
        return max_sum


        