# def rangeSumBST(root, low, high):
# from collections import deque
# from bisect import bisect_left, bisect_right
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

root.right = TreeNode(15)
root.right.left = TreeNode(None)
root.right.right = TreeNode(18)
#
#
# def tree_to_list(root):
#     lst = []
#     if not root:
#         return lst
#
#     q = deque([root])
#     while q:
#         node = q.popleft()
#         if node:
#             if node.val is not None:
#                 lst.append(node.val)
#                 q.append(node.left)
#                 q.append(node.right)
#     return sorted(lst)
#
# def rangeSumBST(root, low, high):
#     lst = tree_to_list(root)
#
#     low_index = bisect_left(lst, low)
#     right_index = bisect_right(lst, high)
#
#     result = 0
#     for i in range(low_index, right_index):
#         result += lst[i]
#
#     return result
#


def rangeSumBST(root, L, R):
    def dfs(node: TreeNode):
        if not node:
            return 0

        if node.val < L:
            return dfs(node.right)
        elif node.val > R:
            return dfs(node.left)
        return node.val + dfs(node.left) + dfs(node.right)

    return dfs(root)

print(rangeSumBST(root, 7, 15))