# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head1 = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        head2 = slow.next
        slow.next = None

        prev = None
        cur = head2

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        head2 = prev

        while head2:
            tmp1 = head1.next
            head1.next = head2
            tmp2 = head2.next
            head2.next = tmp1
            head1 = tmp1
            head2 = tmp2
        
        



        
