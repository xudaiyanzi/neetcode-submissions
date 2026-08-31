class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        count, n = len(self.stack_in), len(self.stack_in)
        while count > 0:
            out = self.stack_in.pop()
            self.stack_out.append(out)
            count -= 1
        self.stack_in.append(x)
        while count < n:
            out = self.stack_out.pop()
            self.stack_in.append(out)
            count += 1

    def pop(self) -> int:
        return self.stack_in.pop()

    def peek(self) -> int:
        return self.stack_in[-1]

    def empty(self) -> bool:
        return len(self.stack_in) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()