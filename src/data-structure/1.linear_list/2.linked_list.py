class Node(object):
    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next = next_node


class SinglyLinkedList(object):
    """带头节点的单链表
    元素是从下标为1开始存储"""

    def __init__(self) -> None:
        self.head = Node('head')

    def insert_to_head(self, value):
        """在链头插入"""
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node
        return True

    def insert_after(self, node, value):
        """在指定节点之后插入"""
        if node is None:
            return False
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        return True

    def insert_before(self, node, value):
        """在指定节点之前插入
        思路：在节点之后插入并交换数据域"""
        if node is None:
            return False
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        new_node.data, node.data = node.data, new_node.data
        return True

    def insert_by_index(self, index, value):
        """按位序插入节点"""
        if index < 1:
            self.insert_to_head(value)
            return True

        new_node = Node(value)
        current_index = 0
        current_node = self.head
        while current_node is not None and current_index < index - 1:
            current_index += 1
            current_node = current_node.next
        if current_node is None:
            return False

        new_node.next = current_node.next
        current_node.next = new_node
        return True

    def delete_by_index(self, index):
        """删除指定位置的节点"""
        if index < 1:
            return False
        current_index = 0
        current_node = self.head
        while current_node is not None and current_index < index - 1:
            current_index += 1
            current_node = current_node.next
        if current_node is None:
            return False

        current_node.next = current_node.next.next
        return True

    def delete_by_node(self, node):
        """删除指定节点:
        方法1: 传入头指针, 循环寻找node的前驱结点
        方法2: 类似结点前插的实现。有坑，指定结点是最后一个结点时，需要特殊处理"""
        current_node = self.head
        while current_node is not None and current_node.next != node:
            current_node = current_node.next

        if current_node is None:
            return False
        current_node.next = node.next
        return True

    def find_by_value(self, value: object) -> Node | None:
        """按值查找"""
        current_node = self.head.next

        while (current_node is not None) and (current_node.data != value):
            current_node = current_node.next
        return current_node

    def find_by_index(self, index: int) -> Node | None:
        """按位查找"""
        if index < 0:
            return False

        current_node = self.head
        current_index = 0
        while (current_node is not None) and (current_index != index):
            current_node = current_node.next
            current_index += 1

        if current_node is None:
            return False
        return current_node

    def get_length(self):
        """求表长"""
        len = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            len += 1
        return len

    def print_all(self):
        """打印链表节点"""
        current = self.head
        print(f'{current.data}', end='')
        current = current.next
        while current:
            print(f'-> {current.data}', end='')
            current = current.next
        print('\n', flush=True)

    def reversed_self(self):
        """反转链表"""
        current_node = self.head
        pre = None
        while current_node:
            tmp = current_node.next
            current_node.next = pre
            pre = current_node
            current_node = tmp
        self.head = pre

    def has_ring(self):
        """检查链表中是否有环并返回环的入口"""
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                # 判断环入口位置
                index1 = fast
                index2 = self.head
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return index1
        return False

    def delete_last_n_node(self, n):
        """删除链表中倒数第N个节点"""
        fast, slow = self.head, self.head
        while n >= 0:
            n -= 1
            fast = fast.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

    def swap_node(self):
        """两两交换链表中的节点"""
        pre = self.head
        while pre.next and pre.next.next:
            current = pre.next
            post = pre.next.next

            pre.next = post
            current.next = post.next
            post.next = current

            pre = pre.next.next

    def get_intersection_node(self, list_a, list_b):
        """判断链表是否相交并返回相交点"""
        len_a, len_b = 0, 0
        cur = list_a
        while cur:  # 求链表a的长度
            cur = cur.next
            len_a += 1

        cur = list_b
        while cur:  # 求链表b的长度
            cur = cur.next
            len_b += 1

        cur_a, cur_b = list_a, list_b

        if len_a > len_b:  # 让curB为最长链表的头，lenB为其长度
            cur_a, cur_b = list_b, list_a
            len_a, len_b = len_b, len_a
        for _ in range(len_b - len_a):  # 让curA和curB在同一起点上（末尾位置对齐）
            cur_b = cur_b.next

        while cur_a:  # 遍历curA 和 curB，遇到相同则直接返回
            if cur_a == cur_b:
                return cur_a
            else:
                cur_a = cur_a.next
                cur_b = cur_b.next

        return None


l = SinglyLinkedList()
for i in range(10):
    l.insert_to_head(i)
l.print_all()

l.swap_node()
l.print_all()

l.delete_last_n_node(3)
l.print_all()

node = l.find_by_value(2)
l.insert_after(node, 10)
print('insert value=2：')
l.print_all()

node2 = l.find_by_index(2)
l.insert_before(node2, 11)
l.print_all()

l.insert_by_index(1, 12)
l.print_all()

l.delete_by_index(3)
print('删除index=3后：')
l.print_all()

node3 = l.find_by_value(5)
l.delete_by_node(node3)
print('value=5后：')
l.print_all()

l.reversed_self()
l.print_all()

print(l.has_ring())
