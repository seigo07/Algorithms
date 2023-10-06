# 与えられた文字列が回文（文字列が前から読んでも後ろから読んでも同じか）かどうかを判定する


def isPalindrome(s):

    # 文字列を小文字に変換し、文字と数字以外の文字を無視
    # ''.joinにより、文字列間に何も挿入され図、リスト内の各文字がそのまま連結される
    s = ''.join(e.lower() for e in s if e.isalnum())

    # 文字列が前から読んでも後ろから読んでも同じかどうかを判定
    # s[::-1]はsの逆文を表す
    return s == s[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))  # Returns True
print(isPalindrome("race car"))  # Returns True
print(isPalindrome("Hello, world"))  # Returns False

