class Solution(object):
    def deleteDuplicates(self, head):
        slow=head
        while (slow and slow.next!=None):
            if(slow.val==slow.next.val):
             slow.next=slow.next.next
            else:
                slow=slow.next
        return head

       