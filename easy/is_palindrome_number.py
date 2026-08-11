# 整数xが、前から読んでも後ろから読んでも同じ「回文数」かを判定
# 時間・空間計算量：O(n)

def is_palindrome_number(x: int) -> bool:
    # 整数を文字列に変換し、反転した文字列と比較する
    text = str(x)
    return text == text[::-1]


# 実行例
x = 121
print(is_palindrome_number(x))  # True


