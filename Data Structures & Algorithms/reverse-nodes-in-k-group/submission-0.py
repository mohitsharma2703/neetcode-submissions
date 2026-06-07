# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head 
        cnt = 0
        while cnt < k:
            if temp == None:
                return head 
            temp = temp.next 
            cnt +=1 
        prevNode = self.reverseKGroup(temp,k)
        temp= head 
        cnt = 0
        while cnt < k:
            next = temp.next 
            temp.next = prevNode
            prevNode = temp
            temp = next 
            cnt = cnt+1
        return prevNode
        