# 文字列の ()[]{} が 正しく対応して閉じているか を判定
# 時間・空間計算量: O(n)
def is_valid(s):
    stack = []
    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    for c in s:
        # 開き括弧なら積む
        if c in pairs.values():
            stack.append(c)
        # 閉じ括弧なら対応確認
        else:
            if not stack or stack.pop() != pairs[c]:
                return False
    # stackが空の場合、全てのカッコが対応されているため、Trueを返す
    return len(stack) == 0


# テストケース
print(is_valid("()"))  # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))  # False
print(is_valid("([)]"))  # False
print(is_valid("{[]}"))  # True
