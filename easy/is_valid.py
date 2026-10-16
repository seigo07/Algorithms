# 文字列の ()[]{} が正しく対応して閉じているかを判定

# 1. 開き括弧ならスタックに追加する
# 2. 閉じ括弧ならスタックの最後の開き括弧と対応するか確認する
# 3. 最後にスタックが空なら True、残っていれば False

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
    return not stack


# テストケース
print(is_valid("()"))  # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))  # False
print(is_valid("([)]"))  # False
print(is_valid("{[]}"))  # True
