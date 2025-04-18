
'''
与えられた整数 x が回文数かどうかを判定
'''


def is_palindrome(x: int) -> bool:
    # 負の数は回文ではない（-121 → 121- と逆になる）
    if x < 0:
        return False
    # 整数を文字列に変換し、逆順と比較
    return str(x) == str(x)[::-1]

# 実行例
print(is_palindrome(121))    # True
print(is_palindrome(-121))   # False
print(is_palindrome(10))     # False
