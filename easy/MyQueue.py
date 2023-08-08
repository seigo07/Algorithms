class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> int:
        return not self.s1 and not self.s2

queue = MyQueue()

queue.push(1)
print(queue.empty())  # Falseを出力
print(queue.peek())  # 1を出力

queue.push(2)
print(queue.peek())  # 1を出力

print(queue.pop())  # 1を出力
print(queue.peek())  # 2を出力

print(queue.pop())  # 2を出力
print(queue.empty())  # Trueを出力
