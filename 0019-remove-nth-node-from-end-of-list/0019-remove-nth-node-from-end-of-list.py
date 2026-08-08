# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy=ListNode()
        dummy.next=head
        slow=dummy
        fast=dummy
        for _ in range(n+1):
            fast=fast.next
        while fast!=None:
            fast=fast.next
            slow=slow.next
            
        slow.next=slow.next.next
        return dummy.next