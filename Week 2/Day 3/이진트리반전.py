from collections import deque

lst = [4, 2, 7, 1, 3, 6, 9]


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


def test_invert(lst):
    if not lst:
        return []

    def invert(parent):
        if parent:
            parent.left, parent.right = invert(parent.right), invert(parent.left)
            return parent

    root = make_tree(lst, 0)
    return make_lst(invert(root))


def make_lst(root):
    if not root:
        return []

    lst = []
    q = deque([root])

    while q:
        node = q.popleft()
        lst.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return lst


print(test_invert(lst))
