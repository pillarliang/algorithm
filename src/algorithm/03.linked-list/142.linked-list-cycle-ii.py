#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = low = head
        while fast and fast.next:
            fast = fast.next.next
            low = low.next

            if fast == low:
                # exist circle
                index1 = head
                index2 = fast
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return index1
        return None


# @lc code=end
