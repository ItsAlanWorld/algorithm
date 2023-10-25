from collections import deque
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


def diameterOfBinaryTree(root):
    max_length = 0

    def dfs(node):
        nonlocal max_length
        if node is None:
            return 0

        left_length = dfs(node.left)
        right_length = dfs(node.right)

        max_length = max(max_length, left_length + right_length)

        return 1 + max(left_length, right_length)

    dfs(root)

    return max_length
root = make_tree([1,2],0)

print(diameterOfBinaryTree(root))

