# プッシュ、ポップ、トップ、および最小要素の一定時間での取得をサポートするスタックを設計します。
# 通常のスタックの機能に加えて、最小の要素をO(1)の時間複雑度で取得する機能を持つスタックを設計する
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        # 新しい要素が現在の最小値よりも小さい、またはmin_stackが空の場合、新しい要素をmin_stackに追加
        # そうでない場合、現在の最小値（min_stackの最後の要素）をmin_stackに再度追加
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None


# 使用例
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # -3 を返す
min_stack.pop()
print(min_stack.top())     # 0 を返す
print(min_stack.getMin())  # -2 を返す
