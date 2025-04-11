
'''
2つのスタックを使用して、FIFO（First-In-First-Out）キューの
すべての機能（push、peek、pop、empty）を実装する
'''


class MyQueue:
    def __init__(self):
        self.s1 = []  # 入力スタック（push専用）
        self.s2 = []  # 出力スタック（pop/peek専用）

    # s1に要素を追加するだけ
    def push(self, value):
        self.s1.append(value)

    # 最も古い要素を取り出す
    def pop(self):
        # s2が空の場合、s1から要素をすべて取り出して逆順にs2に移動する
        # これにより、最も古い要素がs2の先頭にくるようになる
        self.peek()
        # s2から要素を取り出し、FIFOの動作を実現
        return self.s2.pop()

    # キューの最後の要素（キューの先頭要素）を取得（取り出しは行わない）
    def peek(self):
        # popと同じ処理（取り出しは行わない）
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        # スタックの最後の要素を取得する（キューの先頭にある要素）
        return self.s2[-1]

    def empty(self):
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