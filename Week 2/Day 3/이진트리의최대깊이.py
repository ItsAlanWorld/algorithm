from collections import deque

lst = [3, 9, 20, None, None, 15, 7]


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree(lst, index):
    parent = None
    if index < len(lst):
        value = lst[index]
        if value == None:
            return

        parent = TreeNode(value)
        parent.left = make_tree(lst, 2 * index + 1)
        parent.right = make_tree(lst, 2 * index + 2)

    return parent


def max_depth(lst):
    root = make_tree(lst, 0)
    if not root:
        return 0

    q = deque([root])
    depth = 0

    while q:
        depth += 1
        for _ in range(len(q)):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    return depth


print(max_depth(lst))
