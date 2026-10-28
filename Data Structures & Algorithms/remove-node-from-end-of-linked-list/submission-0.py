# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()         
        dummy.next = head
        slow = fast = head
        prev = dummy
        count = n

        while fast.next:
            fast = fast.next
            if count > 1:
                count -= 1
                continue
            prev = slow
            slow = slow.next

        prev.next = slow.next

        return dummy.next