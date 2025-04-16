
# 与えられた文字列 s から作成可能な最長の回文の長さを求める

from collections import Counter


def longest_palindrome(s):
    count = Counter(s)  # 文字ごとの出現回数をカウント
    length = 0
    odd_found = False
    # 各文字とその出現回数に対して処理を行う
    for char, freq in count.items():
        length += (freq // 2) * 2   # 各文字の偶数分を回文の左右に使えるように加算
        # 奇数個の文字があれば、1文字だけ中央に置ける
        if freq % 2 == 1:
            odd_found = True

    # 中央に1文字だけ置ける場合 +1
    if odd_found:
        length += 1

    return length

print(longest_palindrome("abccccdd"))   # 出力: 7
print(longest_palindrome("a"))          # 出力: 1
