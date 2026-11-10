# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        haveMet = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is None: return False
            if fast==slow:
                if haveMet==False:
                    #both meet -> there must be a cycle
                    #reset fast to the head-> the point where the meet will be the cycle
                    fast = head
                    haveMet = True
                else:
                    return True
            