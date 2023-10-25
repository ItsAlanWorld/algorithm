class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        if not self.top:
            return True
        return False

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top is None:
            return False

        self.top = self.top.next
        return self.top.data



