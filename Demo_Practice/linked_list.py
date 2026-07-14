# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     def removeElements(self, head, val):

#         dummy = ListNode(0)
#         dummy.next = head

#         prev = dummy
#         curr = head

#         while curr is not None:

#             if curr.val == val:
#                 prev.next = curr.next
#             else:
#                 prev = curr

#             curr = curr.next

#         return dummy.next   

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

class Solution(object):
    def middleNode(self, head):
        slow=head
        fast=head
        
        while(fast!=None and fast.next!=None):
           
             slow=slow.next
             fast=fast.next.next
        return slow