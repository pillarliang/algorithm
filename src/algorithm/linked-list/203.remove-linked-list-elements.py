from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# without head not by default
"""设置头结点"""


class Solution:
    def removeElements(self, head: Optional[ListNode],
                       val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)

        cur = dummy_head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy_head.next


"""不设头结点"""


class Solution2:
    def removeElements(self, head: Optional[ListNode],
                       val: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            if curr.val == val:  # cases 1-3
                if prev:  # cases 1-2
                    prev.next = curr.next
                else:  # case 3
                    head = curr.next
                curr = curr.next  # for all cases
            else:  # case 4
                prev, curr = curr, curr.next
        return head
