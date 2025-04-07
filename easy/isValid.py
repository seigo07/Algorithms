
'''
文字列内の括弧が「正しく開閉しているか」を判定
最初に開いた括弧が最初に閉じられなければならない
'''

def is_valid(s):

    # 開き括弧格納用
    stack = []

    # 閉じ括弧に対応する開き括弧を定義
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map:
            top = stack.pop() if stack else '#'
            # 閉じ括弧の場合、stackの最後の要素と対応する開き括弧かどうかをチェック
            if bracket_map[char] != top:
                return False
        else:
            # 開き括弧の場合、stackに追加
            stack.append(char)

    # stackが空ならすべて正しく閉じられているため True
    return not stack


# テストケース
print(is_valid("()"))  # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))  # False
print(is_valid("([)]"))  # False
print(is_valid("{[]}"))  # True
