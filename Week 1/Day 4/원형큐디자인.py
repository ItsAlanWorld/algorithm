class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.q = [None] * self.k
        self.f_pointer = 0
        self.b_pointer = (self.k+1) * -1

    def enQueue(self, value: int) -> bool:
        if self.f_pointer == self.k:
            return False
        self.q[self.f_pointer] = value
        self.f_pointer += 1
        self.b_pointer += 1
        print(self.q, self.f_pointer,self.b_pointer)
        return True


    def deQueue(self) -> bool:
        if self.q[0] is not None:
            self.q = self.q[1:]
            while len(self.q) != self.k:
                self.q.append(None)
            self.f_pointer -= 1
            self.b_pointer -= 1
            print(self.q, self.f_pointer,self.b_pointer)

            return True

        return False

    def Front(self) -> int:
        if self.q[0] is not None:
            return self.q[0]
        return -1

    def Rear(self) -> int:
        if self.q[0] is not None:
            return self.q[self.b_pointer]
        return -1

    def isEmpty(self) -> bool:
        if self.q[0] is not None:
            return False
        return True

    def isFull(self) -> bool:
        if self.f_pointer == self.k:
            return True
        return False
