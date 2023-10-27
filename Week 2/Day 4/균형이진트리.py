from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(4)


def isBalanced(root):
    if root is None:
        return True

    def dfs(node, level):
        if node:
            if node.left:
                return dfs(node.left, level + 1)
            else:
                return dfs(node.right, level + 1)
        return level

    return abs(dfs(root.left, 0) - dfs(root.right, 0)) <= 1


