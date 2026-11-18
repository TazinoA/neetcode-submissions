"""
have 2 queues, keep one empty
to push to top of stack, push val to empty queue then empty the prev full queue by popping all to the empty one and repeat
"""
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        if not self.q1 and not self.q2:
            self.q1.append(x)
        elif self.q1:
            self.q2.append(x)
            while self.q1:
                self.q2.append(self.q1.popleft())
        else:
            self.q1.append(x)
            while self.q2:
                self.q1.append(self.q2.popleft())

    def pop(self) -> int:
        if self.q1:
            return self.q1.popleft()
        return self.q2.popleft()

    def top(self) -> int:
        if self.q1:
            return self.q1[0]
        return self.q2[0]

    def empty(self) -> bool:
        if self.q1 or self.q2:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()