
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr= head

        while curr:
            next_temp= curr.next
            curr.next = prev
            prev= curr
            curr=next_temp
        return prev
        