class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def DFS(root: Node):
    if not root: return 'xxx'
    stack = [root]
    while stack:
        cur = stack.pop()
        # xx
        if cur.right: stack.append(cur.right)
        if cur.left: stack.append(cur.left)
        
    return 'xxx'
    

from collections import deque
def BFS(root: Node):
    if not root: return 'xxx'
    queue = deque([root])
    while queue:
        cur = queue.popleft()
        # xx
        if cur.left: queue.append(cur.left)
        if cur.right: queue.append(cur.right)
    
    return 'xxx'
    
    
    
def recursive(root: Node):
    if not root: return 'xxx'
    left_v = recursive(root.left)
    right_v = recursive(root.right)
    return 'xxx'
    