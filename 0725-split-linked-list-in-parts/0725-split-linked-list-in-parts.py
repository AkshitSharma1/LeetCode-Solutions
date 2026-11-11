# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        dummy = ListNode(-1,head)
        list_length = 0
        curr = head
        while curr:
            curr = curr.next
            list_length +=1
        
        #we have k parts each of length list_length//k + 1 if required
        ans = []
        prev = dummy
        curr = head

        for part_num in range(k):
            part_length = list_length//k + (1 if part_num<list_length%k else 0)
            if part_length==0:
                ans.append(None)
                continue
            else:
                part_start = curr
                for _ in range(part_length-1):
                    curr = curr.next

                #disconnect this part
                nxt = curr.next
                curr.next = None
                curr = nxt
                ans.append(part_start)
        return ans
        