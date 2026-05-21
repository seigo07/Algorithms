# 2つのスタックを使用して、FIFO QUEUEのすべての機能（push、peek、pop、empty）を実装する
class myqueue:
    def __init__(self):
        self.in_stack = []  # push用
        self.out_stack = [] # pop / peek 用

    # 新しい要素は in_stack に積む
    def push(self, value):
        self.in_stack.append(value)

    # out_stack が空なら in_stack から移す
    def pop(self):
        # out_stack が空なら in_stack を逆順に移す
        # これにより、最初に入れた値が out_stack の末尾に来るので FIFO になる
        self.peek()
        return self.out_stack.pop()

    # 先頭要素を見る（取り出しは行わない）
    def peek(self):
        # out_stack が空の時だけ移動して FIFO 順にする
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        # out_stackの最後の要素を取得する（キューの先頭にある要素）
        return self.out_stack[-1]

    # 両方空なら Queue も空
    def empty(self):
        return not self.in_stack and not self.out_stack


queue = myqueue()

queue.push(1)
print(queue.empty())  # Falseを出力
print(queue.peek())  # 1を出力

queue.push(2)
print(queue.peek())  # 1を出力

print(queue.pop())  # 1を出力
print(queue.peek())  # 2を出力

print(queue.pop())  # 2を出力
print(queue.empty())  # Trueを出力