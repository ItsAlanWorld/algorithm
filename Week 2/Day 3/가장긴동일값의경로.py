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

        left = left_length + 1 if node.left and node.left.val == node.val else 0
        right = right_length + 1 if node.right and node.right.val == node.val else 0

        max_length = max(max_length, left + right)

        return max(left, right)


    dfs(root)

    return max_length
root = make_tree([5,4,5,1,1,None,5],0)

print(diameterOfBinaryTree(root))

