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
        # out_stackが空の場合、in_stackから要素をすべて取り出して逆順にout_stackに移動する
        # これにより、最も古い要素がout_stackの先頭にくるようになる
        self.peek()
        # out_stackから要素を取り出し、FIFOの動作を実現
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