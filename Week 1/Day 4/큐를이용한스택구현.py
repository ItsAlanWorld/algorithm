import collections

class MyStack:
    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()

    def push(self, x: int) -> None:
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft())


    def pop(self) -> int:
        if self.q1:
            return self.q1.popleft()

    def top(self) -> int:
        if self.q1:
            return self.q1[0]

    def empty(self) -> bool:
        return not self.q1
    # def __init__(self):
    #     self.q = collections.deque()
    #
    # def push(self, x: int) -> None:
    #     self.q.append(x)
    #     for _ in range(len(self.q) -1):
    #         self.q.append(self.q.popleft())
    #
    # def pop(self) -> int:
    #     return self.q.popleft()
    #
    # def top(self) -> int:
    #     return self.q[0]
    #
    # def empty(self) -> bool:
    #     return len(self.q) == 0


