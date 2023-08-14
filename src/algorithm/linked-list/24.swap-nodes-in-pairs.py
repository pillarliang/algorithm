#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur_node = dummy_head

        while cur_node.next and cur_node.next.next:
            second_node = cur_node.next
            third_node = second_node.next

            cur_node.next = third_node
            second_node.next = third_node.next
            third_node.next = second_node

            cur_node = second_node

        return dummy_head.next


# @lc code=end
head = [1, 2, 3, 4]
print(Solution().swapPairs(head))
