# 文字 '('、')'、'{'、'}'、'['、および ']' のみを含む文字列 s を指定
# 開き括弧と閉じ括弧は同じタイプである必要がある
# 最初に開いた括弧が最初に閉じられなければならない


# def isValid(s):
#     mapping = {
#         "(": ")",
#         "[": "]",
#         "{": "}"
#     }
#     stack = []
#     last_index = len(s) - 1
#     for i, c in enumerate(s):
#         if c in mapping:
#             stack.append(c)
#         else:
#             popped_element = stack.pop()
#             if mapping[popped_element] == c:
#                 if not stack and last_index == i:
#                     return True
#             else:
#                 return False


def isValid(s):
    stack = []
    # 閉じカッコと開きカッコの対応関係をマッピング
    mapping = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    # 1文字ずつループ
    for char in s:
        # 閉じカッコの場合
        if char in mapping.values():
            # 開きカッコの場合、スタックに追加
            stack.append(char)
        else:
            # スタックが空の場合、閉じカッコに対応する開きカッコがないので無効
            if not stack:
                return False
            # 閉じカッコに対応する開きカッコをstackから取り出す
            top_bracket = stack.pop()
            # 対応する開きカッコでない場合、無効
            if mapping[char] != top_bracket:
                return False
    # stackが空の場合、全てのカッコが対応されているため、Trueを返す。
    return not stack


# テストケース
print(isValid("()"))  # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))  # False
print(isValid("([)]"))  # False
print(isValid("{[]}"))  # True
