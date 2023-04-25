from collections import deque


class TreeNode(object):

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class NoRecursiveTraveral(object):
    """非递归遍历"""

    def pre_order(self, root):
        """先序遍历"""
        stack = []
        result = []
        cur = root
        while cur or stack:
            # 先访问当前结点再入栈
            if cur:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right
        return result

    def in_order(self, root: TreeNode):
        """中序遍历："""
        stack = []
        result = []
        cur = root
        while cur or stack:
            # 先迭代访问最底层的左子树结点
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                # 到达最左结点后处理栈顶结点
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result

    def pos_order(self, root: TreeNode):
        """后序遍历"""
        stack = []
        result = []
        cur = root
        rec = None  # 记录最近访问过的结点
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                # 栈顶元素出栈并访问∶
                cur = stack[-1]
                if cur.right and cur.right != rec:
                    # 若右子树存在且未访问过
                    cur = cur.right
                else:
                    cur = stack.pop()
                    result.append(cur.val)
                    rec = cur
                    cur = None
        return result

    def level_order(self, root: TreeNode):
        """层序遍历"""
        result = []
        if root is None:
            return result
        queue = deque([root])
        while queue:
            sub_res = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                sub_res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(sub_res)
        return result
