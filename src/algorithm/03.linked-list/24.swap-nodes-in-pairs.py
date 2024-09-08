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

    def swapPairs_old(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        prev = dummy_node  # prev 来跟踪每对需要交换的节点的前置节点.⚠️

        while (
            prev.next and prev.next.next
        ):  #  检查 prev 后面是否至少有两个节点可以交换。
            first = prev.next
            second = prev.next.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first  # 将 prev 移动到 first，为下一次交换做好准备。

        return dummy_node.next


# @lc code=end
head = [1, 2, 3, 4]
print(Solution().swapPairs(head))
