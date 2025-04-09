# 与えられた文字列が回文（文字列が前から読んでも後ろから読んでも同じか）かどうかを判定する


def is_palindrome(s):

    # 文字列を小文字に変換。
    # 文字と数字以外の文字を無視
    # ''.joinにより、文字列間に何も挿入されず、リスト内の各文字がそのまま連結される
    s = ''.join(e.lower() for e in s if e.isalnum())

    # 文字列が前から読んでも後ろから読んでも同じかどうかを判定
    # s[::-1]は s の逆文を表す
    return s == s[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))  # Returns True
print(is_palindrome("race car"))  # Returns True
print(is_palindrome("Hello, world"))  # Returns False

