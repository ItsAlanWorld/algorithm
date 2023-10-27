from collections import deque

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def deserialize(data):

    values = data.split()
    if values[0] != "#":
        root = TreeNode(int(values[0]))
    else:
        return []
    q = deque([root])
    index = 1
    while q:
        node = q.popleft()
        if index < len(values) and values[index] != '#':
            node.left = TreeNode(int(values[index]))
            q.append(node.left)
        index += 1
        if index < len(values) and values[index] != '#':
            node.right = TreeNode(int(values[index]))
            q.append(node.right)
        index += 1
    return root

def serialize(root):
    q = deque([root])
    result = ['#']
    while q:
        node = q.popleft()
        if node:
            q.append(node.left)
            q.append(node.right)

            result.append(str(node.val))
        else:
            result.append('#')

    while result[-1] == '#':
        result.pop()
    return ' '.join(result)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = None
root.left.right = None
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

serialized = serialize(root)
print(serialized)

print(deserialize(serialized))


