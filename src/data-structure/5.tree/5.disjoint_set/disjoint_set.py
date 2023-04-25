class DisjointSet(object):

    def __init__(self, N) -> None:
        """并查集的初始化操作:
        用数组来存储每个元素的父节点, 初始化时将它们的父节点设为自己。"""
        self.root = [i for i in range(N)]
        self.depth = [1 for i in range(N)]

    def find(self, k):
        """用递归实现元素的查询, 直至根节点（根节点的标志就是父节点是本身）
        每次查找完成之后都直接更新节点的父节点信息为最顶部父节点"""
        if self.root[k] == k:
            return k
        self.root[k] = self.find(self.root[k])
        return self.root[k]

    def union(self, a, b):
        """并查集的合并操作"""
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.root[y] = x
        return

    def union_optimize(self, a, b):
        """并查集的优化：小树合到大树上"""
        x = self.find(a)
        y = self.find(b)
        xh = self.depth[x]
        yh = self.depth[y]
        if x == y:
            return
        if xh >= yh:
            self.root[y] = x
            self.depth[x] = max(self.depth[x], self.depth[y] + 1)
        else:
            self.root[x] = y
            self.depth[y] = max(self.depth[y], self.depth[x] + 1)
