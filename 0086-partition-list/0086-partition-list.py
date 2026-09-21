class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head

        shead = ListNode(0)
        stail = shead

        lhead = ListNode(0)
        ltail = lhead

        while curr:
            if curr.val < x:
                stail.next = curr
                stail = stail.next
            else:
                ltail.next = curr
                ltail = ltail.next

            curr = curr.next

        ltail.next = None
        stail.next = lhead.next

        return shead.next