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

# class Solution(object):
#     def middleNode(self, head):
#         slow=head
#         fast=head
        
#         while(fast!=None and fast.next!=None):
           
#              slow=slow.next
#              fast=fast.next.next
#         return slow     

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false. 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def hasCycle(self, head):
#         slow=head
#         fast=head
#         while(fast!=None and fast.next!=None):
           
#                 fast=fast.next.next
#                 slow=slow.next
#                 if(fast==slow):
#                           return True
            
#         return False

#  Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
 
class Solution(object):
    def nextno(self,n):
        total=0
        while n>0:
            
            digit=n%10
            total=total+digit*digit
            n=n//10
        return total
    
    def isHappy(self, n):
        slow=n
        fast=n
        while True:
             slow=self.nextno(slow)
             fast=self.nextno(self.nextno(fast))
             if (slow==1 or fast==1):
                 return True
             if(slow==fast):
                  return False
         
