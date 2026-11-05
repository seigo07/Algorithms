
# 以下の4つの操作をすべて O(1) で実行するスタックを作る。

# push(val)	値を追加
# pop()	最後の値を削除
# top()	最後の値を取得
# getMin()	最小値を取得

# 基本アルゴリズム: Stack（スタック）＋ Auxiliary Stack（補助スタック）

# 処理フロー
# 1. 初期化：stack（通常の値）と min_stack（最小値）を用意。
# 2. push(val)：stack に値を追加。min_stack に現在の最小値を追加。
# 3. pop()：両方のスタックの末尾を削除。
# 4. top()：stack[-1] を返す。
# 5. getMin()：min_stack[-1] を返す。

# 全ての関数の時間計算量：O(1) 空間計算量：O(n)

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        # 新しい要素が現在の最小値よりも小さい、またはmin_stackが空の場合、新しい要素をmin_stackに追加
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        # そうでない場合、現在の最小値（min_stackの最後の要素）をmin_stackに再度追加
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
