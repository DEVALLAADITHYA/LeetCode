class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = head
        r = head
        while r and r.next:
            l = l.next
            r = r.next.next
            if l == r:
                return True
        return False