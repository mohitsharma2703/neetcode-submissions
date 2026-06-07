# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

    # Step 2: If we need to remove the first node
        if n == length:
            return head.next

    # Step 3: Traverse to the node just before the target
        current = head
        for _ in range(length - n - 1):
            current = current.next

    # Step 4: Remove the target node
        if current.next:
            current.next = current.next.next

        return head