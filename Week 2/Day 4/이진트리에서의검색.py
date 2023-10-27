from collections import deque
from bisect import bisect_left


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(40)
root.left = TreeNode(20)
root.right = TreeNode(60)

root.left.left = TreeNode(10)
root.left.right = TreeNode(30)

root.right.left = TreeNode(50)
root.right.right = TreeNode(70)


def searchBST(root, val):
    result = None
    def bfs(node, val):
        nonlocal result
        if not node:
            return -1
        if node.val == val:
            result = node
            return result
        if node.val > val:
            bfs(node.left, val)
        else:
            bfs(node.right, val)
        return result if result and result.val == val else None

    root = bfs(root, val)
    result = []
    if root is None:
        return result
    q = deque([root])

    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)

    return result

searchBST(root, 20)