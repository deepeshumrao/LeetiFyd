class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        seen = set()
        unique_vals = []
        curr = head
        while curr:
            if curr.val not in seen:
                seen.add(curr.val)
                unique_vals.append(curr.val)
            curr = curr.next

        dummy = ListNode(0)
        tail = dummy
        for val in unique_vals:
            tail.next = ListNode(val)
            tail = tail.next

        return dummy.next