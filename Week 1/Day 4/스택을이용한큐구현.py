class MyQueue:

    # def __init__(self):
    #     self.s1 = []
    #     self.s2 = []
    #
    # def push(self, x: int) -> None:
    #     while self.s1:
    #         self.s2.append(self.s1.pop())
    #     self.s1.append(x)
    #     while self.s2:
    #         self.s1.append(self.s2.pop())
    #
    # def pop(self) -> int:
    #     if self.s1:
    #         return self.s1.pop()
    #
    # def peek(self) -> int:
    #     if self.s1:
    #         return self.s1[-1]
    #
    # def empty(self) -> bool:
    #     return not self.s1
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []