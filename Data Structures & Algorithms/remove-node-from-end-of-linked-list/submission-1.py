# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next =

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers together
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the target node
        slow.next = slow.next.next

        return dummy.next