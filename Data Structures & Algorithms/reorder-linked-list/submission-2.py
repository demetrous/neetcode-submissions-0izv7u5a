# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1.Find middle of the big list  
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2.Split to two lists
        second_head = slow.next
        slow.next = None 
        
        # 3.Reverse the second part
        cur = second_head
        prev = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # 4.Merge back with checker pattern
        second_head = prev

        while second_head:
            tmp1 = head.next
            head.next = second_head
            tmp2 = second_head.next
            second_head.next = tmp1
            head = tmp1
            second_head = tmp2